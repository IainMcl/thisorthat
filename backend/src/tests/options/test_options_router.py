from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_options():
    response = client.get("/options/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    for item in data:
        assert "id" in item
        assert "name" in item
        assert "image_url" in item
        assert "metadata" in item
