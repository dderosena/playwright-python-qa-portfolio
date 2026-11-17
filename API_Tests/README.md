# API Testing with Python and pytest

Personal API automation project using Python, requests, and pytest against JSONPlaceholder.

## Test Coverage

| Test file | What it checks |
| --- | --- |
| test_get_posts.py | GET an existing post; verify status 200, IDs, and a nonempty title |
| test_get_invalid_post.py | GET a nonexistent post; verify status 404 and an empty JSON object |
| test_create_post.py | POST a new post; verify status 201, returned fields, and an ID |
| test_create_invalid_post.py | POST empty title and body fields; verify the API returns status 201 |
| test_update_post.py | PUT an updated post; verify status 200 and updated title and body |

## Tools

- Python
- requests
- pytest

## Setup

From the repository root, with your virtual environment activated:

```bash
python -m pip install requests pytest

