"""
Deterministic business tools for the Business Crisis & Opportunity
Intelligence Agent.

The tools in this module perform calculations and provide controlled
business data to the agent runtime.
"""

from business_data import (
    BUSINESS_CONTEXT,
    BASELINE_FINANCIAL_DATA,
    PILOT_FINANCIAL_DATA,
    BASELINE_PERFORMANCE,
    ALTERNATIVE_SCENARIO,
    POST_PILOT_RESULTS,
)


def get_business_context():
    """Return the core business context."""
    return BUSINESS_CONTEXT.copy()


def get_baseline_performance():
    """Return the baseline hotel performance data."""
    return BASELINE_PERFORMANCE.copy()


def get_alternative_scenario():
    """Return the alternative pricing scenario."""
    return ALTERNATIVE_SCENARIO.copy()


def get_post_pilot_results():
    """Return the controlled post-pilot results."""
    return POST_PILOT_RESULTS.copy()


def calculate_scenario(
    occupancy_rate,
    adr,
    ota_share,
    ota_commission_rate,
):
    """
    Calculate room revenue, OTA commission, and net room revenue
    for a given hotel scenario.
    """

    available_rooms = BUSINESS_CONTEXT["rooms"]
    occupied_rooms = available_rooms * occupancy_rate

    room_revenue = occupied_rooms * adr

    ota_commission = (
        room_revenue
        * ota_share
        * ota_commission_rate
    )

    net_room_revenue = room_revenue - ota_commission

    return {
        "available_rooms": available_rooms,
        "occupancy_rate": occupancy_rate,
        "adr": adr,
        "occupied_rooms": occupied_rooms,
        "room_revenue": room_revenue,
        "ota_share": ota_share,
        "ota_commission_rate": ota_commission_rate,
        "ota_commission": ota_commission,
        "net_room_revenue": net_room_revenue,
    }


def calculate_financial_impact(
    room_revenue,
    operating_cost,
    direct_acquisition_cost,
):
    """
    Calculate contribution and financial change for a scenario.
    """

    contribution = (
        room_revenue
        - operating_cost
        - direct_acquisition_cost
    )

    return {
        "room_revenue": room_revenue,
        "operating_cost": operating_cost,
        "direct_acquisition_cost": direct_acquisition_cost,
        "contribution": contribution,
    }


def compare_financial_impact():
    """
    Compare baseline and pilot financial contribution.
    """

    baseline = calculate_financial_impact(
        BASELINE_FINANCIAL_DATA["room_revenue"],
        BASELINE_FINANCIAL_DATA["operating_cost"],
        BASELINE_FINANCIAL_DATA["direct_acquisition_cost"],
    )

    pilot = calculate_financial_impact(
        PILOT_FINANCIAL_DATA["room_revenue"],
        PILOT_FINANCIAL_DATA["operating_cost"],
        PILOT_FINANCIAL_DATA["direct_acquisition_cost"],
    )

    contribution_change = (
        pilot["contribution"]
        - baseline["contribution"]
    )

    return {
        "baseline": baseline,
        "pilot": pilot,
        "contribution_change": contribution_change,
        "financially_improved": contribution_change > 0,
    }
