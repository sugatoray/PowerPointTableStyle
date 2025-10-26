import reflex as rx
from typing import TypedDict


class QuarterlyMetric(TypedDict):
    metric: str
    q1_2024: str
    q2_2024: str
    q3_2024: str
    q4_2024: str
    yoy_growth: str


class PowerPointTableState(rx.State):
    """State for the PowerPoint style table."""

    table_data: list[QuarterlyMetric] = [
        {
            "metric": "Revenue (in M)",
            "q1_2024": "$1.2M",
            "q2_2024": "$1.5M",
            "q3_2024": "$1.8M",
            "q4_2024": "$2.2M",
            "yoy_growth": "+25%",
        },
        {
            "metric": "New Customers",
            "q1_2024": "1,200",
            "q2_2024": "1,500",
            "q3_2024": "1,850",
            "q4_2024": "2,300",
            "yoy_growth": "+30%",
        },
        {
            "metric": "Customer Churn",
            "q1_2024": "5%",
            "q2_2024": "4.5%",
            "q3_2024": "4.2%",
            "q4_2024": "3.8%",
            "yoy_growth": "-1.2%",
        },
        {
            "metric": "Avg. Order Value",
            "q1_2024": "$150",
            "q2_2024": "$155",
            "q3_2024": "$160",
            "q4_2024": "$165",
            "yoy_growth": "+10%",
        },
        {
            "metric": "Site Traffic (k)",
            "q1_2024": "500k",
            "q2_2024": "550k",
            "q3_2024": "620k",
            "q4_2024": "700k",
            "yoy_growth": "+40%",
        },
    ]
    columns: list[str] = [
        "Key Metric",
        "Q1 2024",
        "Q2 2024",
        "Q3 2024",
        "Q4 2024",
        "YoY Growth",
    ]