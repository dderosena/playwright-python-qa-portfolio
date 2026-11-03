import requests

def test_update_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    payload = {
        "id": 1,
        "title": "Updated API Test",
        "body": "Learning PUT requests with Python",
        "userId": 1
    }

    response = requests.put(
        url,
        json=payload,
        timeout=10
    
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated API Test"
    assert data["body"] == "Learning PUT requests with Python"