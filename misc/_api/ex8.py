import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def create_post(title, body, user_id):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    response = requests.post(url=URL, json=data, headers=headers)

    if response.status_code == 201:
        return response.json()
    else:
        print("Error: ", response.status_code)
        return None


if __name__ == "__main__":
    post = create_post("Hello", "API learning", 1)
    print(post)
