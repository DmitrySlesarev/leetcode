import requests


def fetch_pages(api_url):
    page = 1
    while True:
        data = requests.get(f"{api_url}?page={page}")
        if not data.json()['results']:
            break
        for item in data.json()['results']:
            yield item
        page += 1


if __name__ == "__main__":
    for item in fetch_pages('https://api.example.com/users'):
        print(item)