import reflex as rx


def site_header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.span(
                    rx.icon("cloud", class_name="h-6 w-6 text-[#18A999]"),
                    class_name="flex h-11 w-11 items-center justify-center rounded-2xl border border-[#D6E7E2] bg-white",
                ),
                rx.el.span(
                    rx.el.span(
                        "FoxCloud",
                        dir="ltr",
                        class_name="block text-lg font-bold tracking-tight text-[#132B38]",
                    ),
                    rx.el.span(
                        "فاکس‌کلاد",
                        class_name="block text-[11px] font-medium text-[#60747D]",
                    ),
                    class_name="leading-tight",
                ),
                href="/",
                aria_label="فاکس‌کلاد، صفحه اصلی",
                class_name="flex items-center gap-3",
            ),
            rx.el.nav(
                rx.el.a(
                    "خانه",
                    href="/",
                    class_name="hidden text-sm font-medium text-[#536971] transition-colors hover:text-[#18A999] sm:inline-flex",
                ),
                rx.el.a(
                    "نحوه استفاده",
                    href="/#how-it-works",
                    class_name="hidden text-sm font-medium text-[#536971] transition-colors hover:text-[#18A999] md:inline-flex",
                ),
                rx.el.a(
                    "ابزار پیکربندی",
                    rx.icon("arrow-up-left", class_name="h-4 w-4"),
                    href="/sub",
                    class_name="inline-flex items-center gap-2 rounded-full border border-[#C9D9D6] bg-white px-4 py-2.5 text-xs font-semibold text-[#132B38] transition-colors hover:border-[#18A999] hover:text-[#118577] sm:px-5 sm:text-sm",
                ),
                aria_label="ناوبری اصلی",
                class_name="flex items-center gap-7",
            ),
            class_name="mx-auto flex w-full max-w-5xl items-center justify-between gap-4 px-5 py-5 sm:px-8 sm:py-7",
        ),
        class_name="w-full border-b border-[#E6E9E3] bg-[#F7F7F2]",
    )


def site_footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "FoxCloud",
                    dir="ltr",
                    class_name="text-base font-bold tracking-tight text-[#132B38]",
                ),
                rx.el.p(
                    "راهنمای ساخت پیکربندی؛ نه ارائه‌دهندهٔ سرویس پروکسی.",
                    class_name="mt-2 text-sm leading-7 text-[#60747D]",
                ),
                class_name="text-center sm:text-right",
            ),
            rx.el.div(
                rx.el.a(
                    "صفحه اصلی",
                    href="/",
                    class_name="transition-colors hover:text-[#18A999]",
                ),
                rx.el.a(
                    "ابزار پیکربندی",
                    href="/sub",
                    class_name="transition-colors hover:text-[#18A999]",
                ),
                class_name="flex items-center justify-center gap-6 text-sm font-medium text-[#536971] sm:justify-end",
            ),
            class_name="mx-auto flex w-full max-w-5xl flex-col items-center justify-between gap-6 px-5 py-8 sm:flex-row sm:px-8 sm:py-10",
        ),
        class_name="mt-auto border-t border-[#E6E9E3] bg-[#F7F7F2]",
    )


def site_shell(content: rx.Component) -> rx.Component:
    return rx.el.div(
        site_header(),
        content,
        site_footer(),
        dir="rtl",
        lang="fa",
        class_name="flex min-h-dvh flex-col bg-[#F7F7F2] font-['Vazirmatn'] text-[#132B38] antialiased selection:bg-[#BCECE4]",
    )
