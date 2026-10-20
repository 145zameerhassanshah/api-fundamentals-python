import requests

URL = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    print("=== GET REQUEST ===")
    print("Method:", response.request.method)
    print("URL:", response.request.url)
    print("Status Code:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Response JSON:", response.json())

except requests.RequestException as exc:
    print("Request failed:", exc)
