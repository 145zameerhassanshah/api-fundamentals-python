import requests

URL = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "API Fundamentals",
    "body": "Practicing POST requests with Python requests.",
    "userId": 1
}

try:
    response = requests.post(URL, json=payload, timeout=10)
    response.raise_for_status()

    print("=== POST REQUEST ===")
    print("Method:", response.request.method)
    print("URL:", response.request.url)
    print("Status Code:", response.status_code)
    print("Request Content-Type:", response.request.headers.get("Content-Type"))
    print("Response JSON:", response.json())

except requests.RequestException as exc:
    print("Request failed:", exc)
