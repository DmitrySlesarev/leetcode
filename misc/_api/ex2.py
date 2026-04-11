import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

posts = response.json()

for post in posts[:5]:
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")
    print("-" * 40)