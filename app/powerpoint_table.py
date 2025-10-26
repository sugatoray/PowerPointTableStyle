import reflex as rx
from app.state import PowerPointTableState


def table_header() -> rx.Component:
    """The header for the table."""
    return rx.el.thead(
        rx.el.tr(
            rx.foreach(
                PowerPointTableState.columns,
                lambda column: rx.el.th(
                    column,
                    class_name="px-6 py-4 text-left text-sm font-semibold tracking-wider",
                ),
            ),
            class_name="bg-sky-500 text-white",
        )
    )


def table_row(row_data: dict, index: int) -> rx.Component:
    """A single row in the table body."""
    return rx.el.tr(
        rx.el.td(
            row_data["metric"],
            class_name="px-6 py-4 whitespace-nowrap text-sm font-semibold text-gray-800",
        ),
        rx.el.td(
            row_data["q1_2024"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-600",
        ),
        rx.el.td(
            row_data["q2_2024"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-600",
        ),
        rx.el.td(
            row_data["q3_2024"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-600",
        ),
        rx.el.td(
            row_data["q4_2024"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-600",
        ),
        rx.el.td(
            rx.el.span(
                row_data["yoy_growth"],
                class_name=rx.cond(
                    row_data["yoy_growth"].contains("+"),
                    "text-green-600 font-semibold",
                    "text-red-600 font-semibold",
                ),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-sm",
        ),
        class_name=rx.cond(index % 2 == 0, "bg-white", "bg-gray-50"),
    )


def powerpoint_table() -> rx.Component:
    """The main table component styled like a PowerPoint slide."""
    return rx.el.div(
        rx.el.h1(
            "Quarterly Business Review - 2024",
            class_name="text-2xl font-bold text-gray-800 mb-2",
        ),
        rx.el.p(
            "Performance highlights and key metrics.",
            class_name="text-gray-500 mb-8 text-base",
        ),
        rx.el.div(
            rx.el.table(
                table_header(),
                rx.el.tbody(rx.foreach(PowerPointTableState.table_data, table_row)),
                class_name="min-w-full",
            ),
            class_name="overflow-hidden rounded-lg border border-gray-200",
        ),
        class_name="max-w-5xl w-full bg-white p-8 rounded-xl shadow-[0_4px_8px_rgba(0,0,0,0.15)]",
    )