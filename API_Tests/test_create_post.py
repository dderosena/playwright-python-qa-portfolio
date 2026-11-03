import requests

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "My first API test",
        "body": "Learning API automation with Python",
        "userId": 1
    }

    response = requests.post(
        url,
        json=payload,
        timeout=10

    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data