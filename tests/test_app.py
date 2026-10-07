import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def test_health_check_returns_healthy_service(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "service": "ACEest Fitness & Gym",
        "status": "healthy",
    }


def test_member_can_be_added_and_listed(client):
    create_response = client.post("/members", json={"name": "Aarav", "plan": "premium"})

    assert create_response.status_code == 201
    assert create_response.get_json() == {"id": 1, "name": "Aarav", "plan": "premium"}

    list_response = client.get("/members")
    assert list_response.status_code == 200
    assert list_response.get_json() == {
        "count": 1,
        "members": [{"id": 1, "name": "Aarav", "plan": "premium"}],
    }


def test_member_requires_a_name(client):
    response = client.post("/members", json={"plan": "standard"})

    assert response.status_code == 400
    assert response.get_json() == {"error": "A non-empty member name is required."}