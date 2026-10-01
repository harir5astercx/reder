import reflex as rx

from app.components.site_shell import site_shell
from app.states.sub_state import SubState


INPUT_CLASS = "w-full min-w-0 rounded-xl border border-[#D9E3DE] bg-white px-4 py-3 text-sm text-[#132B38] outline-hidden transition-colors placeholder:text-[#89999B] focus:border-[#18A999] focus:ring-2 focus:ring-[#18A999]/20"


def field(label: str, hint: str, control: rx.Component) -> rx.Component:
    return rx.el.label(
        rx.el.span(label, class_name="block text-sm font-bold text-[#132B38]"),
        control,
        rx.el.span(hint, class_name="block text-xs leading-6 text-[#60747D]"),
        class_name="flex min-w-0 flex-col gap-2",
    )


def configuration_form() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.icon("settings-2", class_name="h-5 w-5 text-[#18A999]"),
            rx.el.h2(
                "مشخصات اتصال", class_name="text-lg font-bold text-[#132B38]"
            ),
            class_name="mb-6 flex items-center gap-3",
        ),
        rx.el.div(
            field(
                "شناسهٔ کاربر (UUID)",
                "شناسه‌ای که روی سرور خودتان تنظیم شده است.",
                rx.el.input(
                    name="uuid",
                    type="text",
                    placeholder="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    dir="ltr",
                    auto_complete="off",
                    class_name=INPUT_CLASS,
                ),
            ),
            field(
                "نشانی سرور",
                "دامنه، IPv4 یا IPv6 سرور سازگار؛ بدون http:// و درگاه.",
                rx.el.input(
                    name="host",
                    type="text",
                    placeholder="example.com",
                    dir="ltr",
                    auto_complete="off",
                    class_name=INPUT_CLASS,
                ),
            ),
            field(
                "درگاه",
                "عددی بین ۱ تا ۶۵۵۳۵.",
                rx.el.input(
                    name="port",
                    type="text",
                    input_mode="numeric",
                    placeholder="443",
                    dir="ltr",
                    auto_complete="off",
                    class_name=INPUT_CLASS,
                ),
            ),
            field(
                "امنیت اتصال",
                "باید با تنظیمات واقعی سرور یکسان باشد.",
                rx.el.div(
                    rx.el.select(
                        rx.el.option("TLS", value="tls"),
                        rx.el.option("بدون TLS", value="none"),
                        name="security",
                        default_value="tls",
                        class_name="w-full appearance-none rounded-xl border border-[#D9E3DE] bg-white px-4 py-3 pl-10 text-sm text-[#132B38] outline-hidden focus:border-[#18A999] focus:ring-2 focus:ring-[#18A999]/20",
                    ),
                    rx.icon(
                        "chevron-down",
                        class_name="pointer-events-none absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-[#60747D]",
                    ),
                    class_name="relative",
                ),
            ),
            field(
                "SNI",
                "در حالت TLS، نام دامنهٔ گواهی سرور را وارد کنید؛ برای بدون TLS خالی بگذارید.",
                rx.el.input(
                    name="sni",
                    type="text",
                    placeholder="example.com",
                    dir="ltr",
                    auto_complete="off",
                    class_name=INPUT_CLASS,
                ),
            ),
            field(
                "مسیر WebSocket",
                "باید با / آغاز شود و با مسیر تنظیم‌شده روی سرور مطابقت کند.",
                rx.el.input(
                    name="path",
                    type="text",
                    placeholder="/your-ws-path",
                    dir="ltr",
                    auto_complete="off",
                    class_name=INPUT_CLASS,
                ),
            ),
            field(
                "نام نمایشی",
                "این نام در انتهای لینک و در کلاینت نشان داده می‌شود.",
                rx.el.input(
                    name="name",
                    type="text",
                    placeholder="سرور شخصی من",
                    auto_complete="off",
                    class_name=INPUT_CLASS,
                ),
            ),
            class_name="grid grid-cols-1 gap-x-5 gap-y-6 sm:grid-cols-2",
        ),
        rx.cond(
            SubState.error != "",
            rx.el.div(
                rx.icon("circle-alert", class_name="h-5 w-5 shrink-0"),
                rx.el.p(SubState.error),
                role="alert",
                class_name="mt-7 flex items-start gap-3 rounded-xl border border-red-200 bg-red-100 px-4 py-3 text-sm leading-7 text-red-700",
            ),
        ),
        rx.el.button(
            rx.icon("wand-sparkles", class_name="h-4 w-4"),
            rx.cond(
                SubState.is_generating, "در حال ساخت...", "ساخت لینک و اشتراک"
            ),
            type="submit",
            disabled=SubState.is_generating,
            class_name="mt-7 inline-flex min-h-12 w-full items-center justify-center gap-2 rounded-xl bg-[#132B38] px-6 py-3 text-sm font-bold text-white transition-colors hover:bg-[#1E4653] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#18A999] disabled:cursor-wait disabled:opacity-60 sm:w-auto",
        ),
        on_submit=SubState.generate,
        class_name="rounded-3xl border border-[#E3E9E4] bg-white p-5 sm:p-8",
    )


def result_block(
    title: str, description: str, value: rx.Var[str], copied: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3(title, class_name="text-sm font-bold text-[#132B38]"),
                rx.el.p(
                    description,
                    class_name="mt-1 text-xs leading-6 text-[#60747D]",
                ),
                class_name="min-w-0",
            ),
            rx.el.button(
                rx.icon("copy", class_name="h-4 w-4"),
                "کپی",
                type="button",
                on_click=[rx.set_clipboard(value), rx.toast(copied)],
                class_name="inline-flex shrink-0 items-center gap-2 rounded-xl border border-[#C9D9D6] bg-white px-4 py-2 text-xs font-semibold text-[#132B38] transition-colors hover:border-[#18A999] hover:text-[#118577] focus-visible:outline-2 focus-visible:outline-[#18A999]",
            ),
            class_name="flex flex-wrap items-start justify-between gap-3",
        ),
        rx.el.pre(
            value,
            dir="ltr",
            class_name="mt-4 max-h-44 w-full overflow-y-auto break-all whitespace-pre-wrap rounded-xl border border-[#E3E9E4] bg-[#F7F7F2] p-4 text-left font-mono text-xs leading-7 text-[#132B38] select-all",
        ),
        class_name="min-w-0",
    )


def output_card() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.icon("file-code-2", class_name="h-5 w-5 text-[#18A999]"),
            rx.el.h2(
                "خروجی آمادهٔ استفاده",
                class_name="text-lg font-bold text-[#132B38]",
            ),
            class_name="flex items-center gap-3",
        ),
        rx.cond(
            SubState.is_generating,
            rx.el.div(
                rx.el.p(
                    "در حال ساخت خروجی...",
                    class_name="text-sm font-medium text-[#536971]",
                ),
                rx.el.div(
                    class_name="mt-4 h-20 animate-pulse rounded-xl bg-[#E3E9E4]"
                ),
                class_name="mt-7",
            ),
            rx.cond(
                SubState.uri != "",
                rx.el.div(
                    result_block(
                        "لینک VLESS",
                        "این لینک را در کلاینت سازگار وارد کنید.",
                        SubState.uri,
                        "لینک VLESS کپی شد.",
                    ),
                    rx.el.div(class_name="h-px w-full bg-[#E3E9E4]"),
                    result_block(
                        "متن اشتراک Base64",
                        "متن کدگذاری‌شدهٔ UTF-8 شامل همین لینک است.",
                        SubState.subscription,
                        "متن اشتراک کپی شد.",
                    ),
                    class_name="mt-7 flex min-w-0 flex-col gap-7",
                ),
                rx.el.div(
                    rx.icon(
                        "link", class_name="mx-auto h-7 w-7 text-[#18A999]"
                    ),
                    rx.el.p(
                        "هنوز خروجی‌ای ساخته نشده است.",
                        class_name="mt-3 text-sm font-semibold text-[#132B38]",
                    ),
                    rx.el.p(
                        "مشخصات سرور خود را وارد کنید و دکمهٔ ساخت را بزنید.",
                        class_name="mt-2 text-xs leading-7 text-[#60747D]",
                    ),
                    class_name="mt-6 rounded-2xl border border-dashed border-[#D9E3DE] bg-[#F7F7F2] px-5 py-10 text-center",
                ),
            ),
        ),
        rx.el.p(
            "متن اشتراک برای کپی و وارد کردن در برنامهٔ سازگار است؛ این یک آدرس اشتراک میزبانی‌شده یا URL به‌روزرسانی خودکار نیست.",
            class_name="mt-7 rounded-xl bg-[#EAF5F1] px-4 py-3 text-xs leading-7 text-[#42645F]",
        ),
        class_name="mt-6 min-w-0 rounded-3xl border border-[#E3E9E4] bg-white p-5 sm:p-8",
    )


def sub_page() -> rx.Component:
    return site_shell(
        rx.el.main(
            rx.el.div(
                rx.el.a(
                    rx.icon("arrow-right", class_name="h-4 w-4"),
                    "بازگشت به خانه",
                    href="/",
                    class_name="inline-flex items-center gap-2 text-sm font-semibold text-[#118577] transition-colors hover:text-[#132B38]",
                ),
                rx.el.div(
                    rx.el.span(
                        "ابزار شخصی پیکربندی",
                        class_name="inline-flex w-fit rounded-full border border-[#CDE4DE] bg-[#EAF5F1] px-3 py-1.5 text-xs font-semibold text-[#118577]",
                    ),
                    rx.el.h1(
                        "ساخت لینک VLESS و اشتراک",
                        class_name="mt-6 text-3xl font-bold leading-relaxed tracking-tight text-[#132B38] sm:text-4xl",
                    ),
                    rx.el.p(
                        "مشخصات سرور سازگار خودتان را وارد کنید تا یک لینک VLESS و متن اشتراک Base64 بسازید. همهٔ مقادیر باید با تنظیمات واقعی سرور مطابقت داشته باشند.",
                        class_name="mt-4 max-w-2xl text-sm leading-8 text-[#536971] sm:text-base sm:leading-9",
                    ),
                    class_name="mt-12 mb-8",
                ),
                configuration_form(),
                output_card(),
                rx.el.div(
                    rx.el.div(
                        rx.icon("server", class_name="h-5 w-5 text-[#18A999]"),
                        class_name="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-[#EAF5F1]",
                    ),
                    rx.el.div(
                        rx.el.h2(
                            "برای اتصال، سرور مستقل لازم است",
                            class_name="text-lg font-bold text-[#132B38]",
                        ),
                        rx.el.p(
                            "این ابزار فقط متن پیکربندی تولید می‌کند؛ نه سرور VLESS اجرا می‌کند و نه ترافیک WebSocket را عبور می‌دهد. ورودی‌ها در پایگاه داده یا فایل ذخیره نمی‌شوند. برای اتصال به سرور سازگار خارجی که خودتان تهیه کرده‌اید نیاز دارید.",
                            class_name="mt-2 text-sm leading-8 text-[#536971]",
                        ),
                    ),
                    class_name="mt-6 flex items-start gap-4 rounded-3xl border border-[#DCE7E2] bg-white p-5 sm:p-8",
                ),
                class_name="mx-auto w-full max-w-4xl px-5 py-12 sm:px-8 sm:py-20",
            ),
            class_name="w-full flex-1",
        )
    )
