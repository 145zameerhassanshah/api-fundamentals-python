import requests

URL = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    print("=== REQUEST ===")
    print("Method:", response.request.method)
    print("URL:", response.request.url)
    print("Headers:", dict(response.request.headers))

    print("\n=== RESPONSE ===")
    print("Status Code:", response.status_code)
    print("Reason:", response.reason)
    print("Headers:", dict(response.headers))
    print("Body:", response.json())

except requests.RequestException as exc:
    print("Request failed:", exc)
