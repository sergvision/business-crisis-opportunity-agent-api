import pytest

from tools import (
    get_business_context,
    get_baseline_performance,
    get_alternative_scenario,
    get_post_pilot_results,
    calculate_scenario,
    calculate_financial_impact,
    compare_financial_impact,
)


def test_business_context():
    context = get_business_context()

    assert context["company_name"] == "Dubai Horizon Hospitality Group"
    assert context["hotels"] == 3
    assert context["rooms"] == 420


def test_baseline_performance():
    baseline = get_baseline_performance()

    assert baseline["occupancy_rate"] == 0.67
    assert baseline["adr"] == 475.0
    assert baseline["ota_share"] == 0.60


def test_alternative_scenario():
    scenario = get_alternative_scenario()

    assert scenario["occupancy_rate"] == 0.66
    assert scenario["adr"] == 465.0


def test_post_pilot_results():
    results = get_post_pilot_results()

    assert results["occupancy_change_pp"] == 6
    assert results["adr_change"] == -20
    assert results["direct_share_change_pp"] == 10


def test_calculate_scenario():
    result = calculate_scenario(
        occupancy_rate=0.67,
        adr=475.0,
        ota_share=0.60,
        ota_commission_rate=0.18,
    )

    assert result["available_rooms"] == 420
    assert result["occupied_rooms"] == pytest.approx(281.4)
    assert result["room_revenue"] == 133665.0
    assert result["ota_commission"] == 14435.82
    assert result["net_room_revenue"] == 119229.18


def test_calculate_financial_impact():
    result = calculate_financial_impact(
        room_revenue=126294.0,
        operating_cost=58000.0,
        direct_acquisition_cost=4200.0,
    )

    assert result["contribution"] == 64094.0


def test_compare_financial_impact():
    result = compare_financial_impact()

    assert result["baseline"]["contribution"] == 64094.0
    assert result["pilot"]["contribution"] == 67004.0
    assert result["contribution_change"] == 2910.0
    assert result["financially_improved"] is True
