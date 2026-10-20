import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_posts_by_user(user_id):
    try:
        response = requests.get(
            f"{BASE_URL}/posts",
            params={"userId": user_id},
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        print("GET failed:", exc)
        return []


def create_post(title, body, user_id):
    payload = {"title": title, "body": body, "userId": user_id}
    try:
        response = requests.post(
            f"{BASE_URL}/posts",
            json=payload,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        print("POST failed:", exc)
        return {}


if __name__ == "__main__":
    print("=== GET WITH QUERY PARAMETER ===")
    posts = get_posts_by_user(1)
    print("Records returned:", len(posts))
    if posts:
        print("First record:", posts[0])

    print("\n=== POST WITH JSON BODY ===")
    print(create_post("Learning APIs", "GET and POST practice", 1))
