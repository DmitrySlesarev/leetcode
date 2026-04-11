import requests

URL = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Content-Type": "application/json"
}

data = {
    "title": "Header test",
    "body": "Testing headers",
    "userId": 1
}

response = requests.post(url=URL, json=data, headers=headers)

if __name__ == "__main__":
    print(response.json())
