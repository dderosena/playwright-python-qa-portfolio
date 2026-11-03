import requests

def test_get_invalid_post():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/999999",
        timeout=10

    )
    assert response.status_code == 404

    data = response.json()

    assert data == {}
