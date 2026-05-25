from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_nearest_stars() -> None:
    response = client.get("/api/v1/stars/nearest")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert data[0]["name"] == "Alpha Centauri"


def test_get_star_by_id() -> None:
    response = client.get("/api/v1/stars/sirius")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == "sirius"
    assert data["name"] == "Sirius"


def test_get_star_by_id_returns_404_when_star_does_not_exist() -> None:
    response = client.get("/api/v1/stars/unknown-star")

    assert response.status_code == 404
