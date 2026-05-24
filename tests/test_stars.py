from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_nearest_stars() -> None:
    response = client.get("/api/v1/stars/nearest")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert data[0]["name"] == "Alpha Centauri"
