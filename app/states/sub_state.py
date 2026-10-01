import base64
import ipaddress
import logging
import re
import uuid
from typing import Any
from urllib.parse import quote, urlencode

import reflex as rx


def _server_address(raw: str) -> tuple[str, str]:
    address = raw.strip()
    bracketed = address.startswith("[") and address.endswith("]")
    candidate = address[1:-1] if bracketed else address
    try:
        ip = ipaddress.ip_address(candidate)
    except ValueError:
        if bracketed or not address or re.fullmatch(r"[0-9.]+", address):
            raise ValueError(
                "نشانی سرور باید یک دامنه یا IP معتبر باشد."
            ) from None
    else:
        if bracketed and ip.version != 6:
            raise ValueError("فقط نشانی IPv6 را داخل کروشه وارد کنید.")
        if ip.version == 6 and ip.scope_id is not None:
            raise ValueError("نشانی IPv6 را بدون شناسهٔ محدوده وارد کنید.")
        normalized = ip.compressed
        return (
            (f"[{normalized}]", f"[{normalized}]")
            if ip.version == 6
            else (normalized, normalized)
        )

    try:
        hostname = address.rstrip(".").encode("idna").decode("ascii").lower()
    except UnicodeError:
        logging.exception("Unexpected error")
        raise ValueError("نام دامنهٔ سرور معتبر نیست.") from None
    if (
        not hostname
        or len(hostname) > 253
        or "." not in hostname
        or any(
            not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?", label)
            for label in hostname.split(".")
        )
    ):
        raise ValueError(
            "نام دامنهٔ سرور را به صورت معتبر، مانند example.com، وارد کنید."
        )
    return hostname, hostname


def _sni_hostname(raw: str) -> str:
    name = raw.strip()
    if not name:
        raise ValueError("برای TLS، نام دامنهٔ SNI را وارد کنید.")
    try:
        ipaddress.ip_address(name)
    except ValueError:
        pass
    else:
        raise ValueError("SNI باید نام دامنه باشد، نه نشانی IP.")
    hostname, _ = _server_address(name)
    return hostname


def _make_output(data: dict[str, Any]) -> tuple[str, str]:
    raw_id = str(data.get("uuid", "")).strip()
    try:
        user_id = str(uuid.UUID(raw_id))
    except (ValueError, AttributeError):
        logging.exception("Unexpected error")
        raise ValueError("شناسهٔ UUID معتبر وارد کنید.") from None

    authority, ws_host = _server_address(data.get("host", ""))
    raw_port = str(data.get("port", "")).strip()
    if (
        not re.fullmatch(r"[0-9]{1,5}", raw_port)
        or not 1 <= int(raw_port) <= 65535
    ):
        raise ValueError("درگاه باید عددی بین ۱ تا ۶۵۵۳۵ باشد.")
    security = str(data.get("security", ""))
    if security not in ("tls", "none"):
        raise ValueError("نوع امنیت را TLS یا بدون TLS انتخاب کنید.")
    raw_sni = str(data.get("sni", "")).strip()
    sni = _sni_hostname(raw_sni) if security == "tls" else ""
    path = str(data.get("path", "")).strip()
    if not path.startswith("/") or any(
        ord(char) < 32 or ord(char) == 127 for char in path
    ):
        raise ValueError(
            "مسیر WebSocket باید با / شروع شود و نویسهٔ کنترلی نداشته باشد."
        )
    name = str(data.get("name", "")).strip()
    if not name or any(ord(char) < 32 or ord(char) == 127 for char in name):
        raise ValueError("یک نام نمایشی معتبر برای اتصال وارد کنید.")

    parameters = [
        ("encryption", "none"),
        ("security", security),
        ("type", "ws"),
        ("host", sni if sni else ws_host),
        ("path", path),
    ]
    if sni:
        parameters.append(("sni", sni))
    uri = f"vless://{user_id}@{authority}:{int(raw_port)}?{urlencode(parameters)}#{quote(name, safe='')}"
    subscription = base64.b64encode("\n".join([uri]).encode("utf-8")).decode(
        "ascii"
    )
    return uri, subscription


class SubState(rx.State):
    uri: str = ""
    subscription: str = ""
    error: str = ""
    is_generating: bool = False

    @rx.event
    def generate(self, form_data: dict[str, Any]):
        self.error = ""
        self.uri = ""
        self.subscription = ""
        self.is_generating = True
        yield
        try:
            uri, subscription = _make_output(form_data)
        except ValueError as e:
            self.error = str(e)
        except Exception as e:
            logging.exception(f"Error: {e}")
            self.error = "ساخت پیکربندی ممکن نشد. ورودی‌ها را بررسی کرده و دوباره تلاش کنید."
        else:
            self.uri = uri
            self.subscription = subscription
        finally:
            self.is_generating = False
