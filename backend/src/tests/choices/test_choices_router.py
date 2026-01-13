from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_post_choice():
    choice_data = {
        "user_id": 1,
        "presented_option_ids": [1, 2],
        "chose_option_id": 1,
    }
    response = client.post("/choices/", json=choice_data)
    assert response.status_code == 201
    assert response.text == "null"
