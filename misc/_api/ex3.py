import requests
from icecream import ic

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params)

# print(response.json())
# ic(response.json())

if response.status_code == 200:
    data = response.json()
    print(type(data))
    print(response.text)
    print(type(response.text))
else:
    print("Error: ", response.status_code)