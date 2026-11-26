
from fastapi.testclient import TestClient
from unittest.mock import patch

from app import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "SUCCESS"
    assert data["case"] == "Case 06"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "SUCCESS"
    assert data["service"] == "business-crisis-opportunity-agent-api"


def test_ask_endpoint_success():
    mock_state = {
        "final_answer": "Test strategic recommendation.",
        "iteration": 2,
        "tool_calls": [],
        "observations": [],
    }

    with patch("app.run_agent", return_value=mock_state):
        response = client.post(
            "/api/v1/ask",
            json={"question": "Analyze hotel performance."},
        )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "SUCCESS"
    assert data["answer"] == "Test strategic recommendation."
    assert data["iteration"] == 2
    assert data["decisionLoop"] == 0


def test_ask_endpoint_empty_question():
    response = client.post(
        "/api/v1/ask",
        json={"question": "   "},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Question cannot be empty."


def test_ask_endpoint_missing_question():
    response = client.post(
        "/api/v1/ask",
        json={},
    )

    assert response.status_code == 422


def test_ask_endpoint_agent_error():
    with patch(
        "app.run_agent",
        side_effect=RuntimeError("Simulated agent failure"),
    ):
        response = client.post(
            "/api/v1/ask",
            json={"question": "Test agent failure."},
        )

    assert response.status_code == 500
    assert "Agent execution failed" in response.json()["detail"]
