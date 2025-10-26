import reflex as rx
from app.powerpoint_table import powerpoint_table


def index() -> rx.Component:
    return rx.el.main(
        powerpoint_table(),
        class_name="font-['JetBrains_Mono'] bg-gray-100 flex items-center justify-center min-h-screen p-4 md:p-8",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)