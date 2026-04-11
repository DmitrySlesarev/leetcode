import requests

def get_posts(user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, params={"userId": user_id})
    return response.json()

print(get_posts(1))