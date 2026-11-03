import requests

def test_create_invalid_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "",
        "body": "",
        "userId": 1
    }

    response = requests.post(
        url,
        json=payload,
        timeout=10

    )

    print("Status code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 201