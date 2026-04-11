import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

data = response.json()

if __name__ == "__main__":
    print(response.status_code)
    print(response.json())

    print(type(data))
    print(data[0])