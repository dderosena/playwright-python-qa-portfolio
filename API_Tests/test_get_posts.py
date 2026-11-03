import requests

def test_get_post():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10

    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1

    assert data["userId"] == 1
    assert isinstance(data["title"], str)
    assert len(data["title"]) > 0