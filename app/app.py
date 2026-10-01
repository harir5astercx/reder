import reflex as rx

from app.components.site_shell import site_shell
from app.pages.sub import sub_page


def step_card(
    number: str, icon: str, title: str, description: str
) -> rx.Component:
    return rx.el.article(
        rx.el.div(
            rx.el.span(
                number, dir="ltr", class_name="text-sm font-bold text-[#18A999]"
            ),
            rx.icon(icon, class_name="h-5 w-5 text-[#18A999]"),
            class_name="flex items-center justify-between",
        ),
        rx.el.h3(title, class_name="mt-9 text-lg font-bold text-[#132B38]"),
        rx.el.p(
            description, class_name="mt-3 text-sm leading-8 text-[#536971]"
        ),
        class_name="flex min-h-56 flex-col rounded-3xl border border-[#E3E9E4] bg-white p-6 sm:p-7",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.span(class_name="h-2 w-2 rounded-full bg-[#18A999]"),
            "راهنمای پیکربندی FoxCloud",
            class_name="mx-auto inline-flex items-center gap-2 rounded-full border border-[#DCE7E2] bg-white px-4 py-2 text-xs font-semibold text-[#42645F] sm:text-sm",
        ),
        rx.el.h1(
            "پیکربندی اتصال،",
            rx.el.br(),
            rx.el.span("بدون پیچیدگی.", class_name="text-[#118577]"),
            class_name="mt-8 text-4xl font-bold leading-[1.55] tracking-tight text-[#132B38] sm:text-5xl sm:leading-[1.45] lg:text-6xl",
        ),
        rx.el.p(
            "فاکس‌کلاد فضایی ساده برای آشنایی با ساخت لینک VLESS و اشتراک از مشخصات سرور خودتان است. اطلاعات اتصال را بشناسید، خروجی را در کلاینت سازگار وارد کنید و کنترل سرورتان را در اختیار داشته باشید.",
            class_name="mx-auto mt-6 max-w-2xl text-base leading-9 text-[#536971] sm:text-lg sm:leading-10",
        ),
        rx.el.div(
            rx.el.a(
                "مشاهده صفحه ابزار",
                rx.icon("arrow-up-left", class_name="h-4 w-4"),
                href="/sub",
                class_name="inline-flex min-h-12 items-center justify-center gap-3 rounded-full bg-[#132B38] px-7 py-3 text-sm font-semibold text-white transition-colors hover:bg-[#1E4653] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#18A999]",
            ),
            rx.el.a(
                "آشنایی با مراحل",
                rx.icon("arrow-down", class_name="h-4 w-4"),
                href="#how-it-works",
                class_name="inline-flex min-h-12 items-center justify-center gap-2 rounded-full border border-[#C9D9D6] bg-white px-6 py-3 text-sm font-semibold text-[#132B38] transition-colors hover:border-[#18A999] hover:text-[#118577]",
            ),
            class_name="mt-9 flex flex-wrap items-center justify-center gap-3",
        ),
        class_name="mx-auto max-w-3xl px-5 pb-18 pt-17 text-center sm:px-8 sm:pb-24 sm:pt-24",
    )


def overview() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "نگاهی کوتاه",
                    class_name="text-xs font-bold tracking-wide text-[#118577]",
                ),
                rx.el.h2(
                    "از مشخصات سرور تا پیکربندی قابل استفاده",
                    class_name="mt-4 max-w-xl text-2xl font-bold leading-relaxed text-[#132B38] sm:text-3xl",
                ),
                rx.el.p(
                    "لینک VLESS مجموعه‌ای از اطلاعات اتصال است: شناسهٔ کاربر، نشانی و درگاه سرور، و تنظیمات انتقال مانند TLS و WebSocket. اشتراک نیز راهی برای ارائهٔ همین لینک‌ها به برنامه‌های سازگار است.",
                    class_name="mt-4 max-w-2xl text-sm leading-8 text-[#536971] sm:text-base sm:leading-9",
                ),
                class_name="max-w-2xl",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "ورودی",
                        class_name="text-xs font-semibold text-[#71848A]",
                    ),
                    rx.el.p(
                        "مشخصات سرور شما",
                        class_name="mt-1 text-sm font-bold text-[#132B38]",
                    ),
                    class_name="min-w-0 flex-1 rounded-2xl border border-[#E3E9E4] bg-[#F7F7F2] px-5 py-4",
                ),
                rx.icon(
                    "arrow-left", class_name="h-5 w-5 shrink-0 text-[#18A999]"
                ),
                rx.el.div(
                    rx.el.span(
                        "خروجی",
                        class_name="text-xs font-semibold text-[#71848A]",
                    ),
                    rx.el.p(
                        "لینک و اشتراک",
                        class_name="mt-1 text-sm font-bold text-[#132B38]",
                    ),
                    class_name="min-w-0 flex-1 rounded-2xl border border-[#DCE7E2] bg-[#EAF5F1] px-5 py-4",
                ),
                class_name="mt-9 flex w-full max-w-2xl items-center gap-3",
            ),
            class_name="rounded-[2rem] border border-[#E3E9E4] bg-white p-6 sm:p-10 lg:p-12",
        ),
        class_name="mx-auto w-full max-w-5xl px-5 sm:px-8",
    )


def how_it_works() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.span(
                "سه قدم روشن", class_name="text-xs font-bold text-[#118577]"
            ),
            rx.el.h2(
                "چطور از پیکربندی استفاده کنم؟",
                class_name="mt-3 text-2xl font-bold leading-relaxed text-[#132B38] sm:text-3xl",
            ),
            rx.el.p(
                "پیش از هر چیز، یک سرور VLESS سازگار و در دسترس لازم دارید.",
                class_name="mt-3 text-sm leading-8 text-[#536971] sm:text-base",
            ),
        ),
        rx.el.div(
            step_card(
                "۰۱",
                "server",
                "سرور خود را آماده کنید",
                "شناسهٔ UUID، دامنه یا نشانی سرور، درگاه و تنظیمات TLS، SNI و مسیر WebSocket را از سرور خود دریافت کنید.",
            ),
            step_card(
                "۰۲",
                "link",
                "اطلاعات را وارد کنید",
                "در ابزار پیکربندی، مشخصات همان سرور را ثبت کنید تا لینک VLESS و متن اشتراک Base64 ساخته شود.",
            ),
            step_card(
                "۰۳",
                "smartphone",
                "در کلاینت وارد کنید",
                "لینک یا اشتراک را در برنامهٔ سازگار با VLESS وارد کنید و فقط پس از بررسی تنظیمات سرور، اتصال را آزمایش کنید.",
            ),
            class_name="mt-9 grid grid-cols-1 gap-4 md:grid-cols-3",
        ),
        id="how-it-works",
        class_name="mx-auto w-full max-w-5xl scroll-mt-8 px-5 py-18 sm:px-8 sm:py-24",
    )


def service_notice() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.icon("info", class_name="h-6 w-6 text-[#53C7B8]"),
                class_name="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl border border-white/20 bg-white/10",
            ),
            rx.el.div(
                rx.el.span(
                    "شفافیت دربارهٔ سرویس",
                    class_name="text-xs font-bold text-[#7BDED0]",
                ),
                rx.el.h2(
                    "این برنامه، سرور پروکسی نیست.",
                    class_name="mt-3 text-2xl font-bold leading-relaxed text-white sm:text-3xl",
                ),
                rx.el.p(
                    "نسخهٔ Reflex Build فاکس‌کلاد هیچ پروکسی VLESS میزبانی نمی‌کند و رلهٔ WebSocket هم نیست. ساخت یک لینک به‌تنهایی اتصال فعال ایجاد نمی‌کند؛ برای استفاده، باید سرور سازگار خودتان را جداگانه تهیه و راه‌اندازی کنید.",
                    class_name="mt-4 max-w-2xl text-sm leading-8 text-[#DAE8E7] sm:text-base sm:leading-9",
                ),
                class_name="min-w-0",
            ),
            class_name="flex flex-col gap-5 rounded-[2rem] bg-[#132B38] p-7 sm:flex-row sm:gap-6 sm:p-10 lg:p-12",
        ),
        class_name="mx-auto w-full max-w-5xl px-5 pb-20 sm:px-8 sm:pb-28",
    )


def index() -> rx.Component:
    return site_shell(
        rx.el.main(
            hero(),
            overview(),
            how_it_works(),
            service_notice(),
            class_name="w-full flex-1",
        )
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/", title="فاکس‌کلاد | راهنمای پیکربندی VLESS")
app.add_page(sub_page, route="/sub", title="ابزار پیکربندی | فاکس‌کلاد")
