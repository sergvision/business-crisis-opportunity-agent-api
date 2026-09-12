"""
Case 06 - Business Crisis & Opportunity Intelligence Agent

Stable business context and controlled demonstration data.
This module contains no secrets and no API credentials.
"""


BUSINESS_CONTEXT = {
    "company_name": "Dubai Horizon Hospitality Group",
    "industry": "Hospitality",
    "location": "Dubai, UAE",
    "properties": 3,
    "total_rooms": 420,
    "customer_mix": [
        "leisure travelers",
        "business travelers",
    ],
    "booking_channels": [
        "direct",
        "OTA",
    ],
    "restaurant": True,
}


BASELINE_METRICS = {
    "occupancy_rate": 0.62,
    "adr": 485.0,
    "ota_share": 0.65,
    "direct_share": 0.35,
    "ota_commission_rate": 0.18,
}


BUSINESS_PROBLEM = {
    "revenue_change_last_3_months": -0.18,
    "operating_cost_change": 0.11,
    "acquisition_cost_increasing": True,
    "problem_summary": (
        "Business performance deteriorated, with declining revenue, "
        "increasing operating costs, and more expensive customer acquisition."
    ),
}


AGENT_ROLE = {
    "role": "Business Intelligence & Strategy Analyst",
    "goal": [
        "Diagnose",
        "Investigate",
        "Analyze",
        "Evaluate",
        "Discover",
        "Recommend",
    ],
    "final_decision_owner": "Human Decision Maker",
}


PRIMARY_SCENARIO = {
    "name": "Controlled Long-Stay Occupancy Development",
    "occupancy_rate": 0.67,
    "adr": 475.0,
    "ota_share": 0.60,
    "ota_commission_rate": 0.18,
}


ALTERNATIVE_SCENARIO = {
    "name": "Controlled Segment-Based Pricing Reset",
    "occupancy_rate": 0.66,
    "adr": 465.0,
    "ota_share": 0.63,
    "ota_commission_rate": 0.18,
}


PILOT_FINANCIAL_DATA = {
    "baseline_room_revenue": 126294,
    "baseline_operating_cost": 58000,
    "baseline_direct_acquisition_cost": 4200,
    "pilot_room_revenue": 132804,
    "pilot_operating_cost": 61000,
    "pilot_direct_acquisition_cost": 4800,
}


EVALUATION_EXPECTATIONS = {
    "decision_tests_total": 3,
    "expected_decision_tests_passed": 3,
    "initial_guardrail_expected": "FAIL",
    "revised_guardrail_expected": "PASS",
    "final_pilot_decision": "SCALE",
    "next_agent_action": "PREPARE_SCALE_UP_PLAN",
}


def get_business_context():
    """Return the stable business context used by the agent."""
    return {
        "business_context": BUSINESS_CONTEXT,
        "baseline_metrics": BASELINE_METRICS,
        "business_problem": BUSINESS_PROBLEM,
        "agent_role": AGENT_ROLE,
    }


def get_scenarios():
    """Return the strategic scenarios used in the controlled demonstration."""
    return {
        "primary": PRIMARY_SCENARIO,
        "alternative": ALTERNATIVE_SCENARIO,
    }


def get_pilot_financial_data():
    """Return controlled pilot financial data."""
    return PILOT_FINANCIAL_DATA
