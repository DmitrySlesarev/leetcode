import requests

URL = "https://jsonplaceholder.typicode.com/posts"

# Method #1: API Key
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url=URL, headers=headers)

# Method #2: API Key in params
params = {
    "api_key": "YOUR_API_KEY"
}

requests.get(url=URL, params=params)