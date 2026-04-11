import requests

URL = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "My first API post",
    "body": "This is sent from Python",
    "userId": 1
}

response = requests.post(url=URL, json=new_post)

if __name__ == "__main__":
    print(f"{response.status_code}")
    print(f"{response.json()}")