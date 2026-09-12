"""
Business data for the Business Crisis & Opportunity Intelligence Agent.

This module contains the controlled business context and financial
data used by the Case 06 API runtime.
"""

BUSINESS_CONTEXT = {
    "company_name": "Dubai Horizon Hospitality Group",
    "location": "Dubai",
    "hotels": 3,
    "rooms": 420,
    "business_model": [
        "Leisure travelers",
        "Business travelers",
    ],
    "booking_channels": [
        "Direct",
        "OTA",
    ],
    "additional_business": [
        "Restaurant",
    ],
}


BASELINE_FINANCIAL_DATA = {
    "room_revenue": 126294.0,
    "operating_cost": 58000.0,
    "direct_acquisition_cost": 4200.0,
}


PILOT_FINANCIAL_DATA = {
    "room_revenue": 132804.0,
    "operating_cost": 61000.0,
    "direct_acquisition_cost": 4800.0,
}


BASELINE_PERFORMANCE = {
    "occupancy_rate": 0.67,
    "adr": 475.0,
    "ota_share": 0.60,
    "ota_commission_rate": 0.18,
}


ALTERNATIVE_SCENARIO = {
    "occupancy_rate": 0.66,
    "adr": 465.0,
    "ota_share": 0.63,
    "ota_commission_rate": 0.18,
}


POST_PILOT_RESULTS = {
    "occupancy_change_pp": 6,
    "adr_change": -20,
    "direct_share_change_pp": 10,
}


BUSINESS_PROBLEM = {
    "revenue_change_percent": -18,
    "operating_cost_change_percent": 11,
    "acquisition_cost_trend": "increased",
}
