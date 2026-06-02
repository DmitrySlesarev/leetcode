import concurrent.futures

import requests
from icecream import ic


def download_file(url, filename):
    ic(f"Downloading {filename}")
    try:
        result = requests.get(url)
        result.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(result.content)
        ic(f"Finished {filename}")
        return True
    except requests.exceptions.RequestException as e:
        ic(f"Failed to download {filename} due to {e}")
        return False


urls = [
    ('https://httpbin.org', 'img1.jpg'),
    ('https://httpbin.org', 'img2.jpg'),
    ('https://httpbin.org', 'img3.jpg')
]


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(download_file, url, filename) for url, filename in urls]

    for future in concurrent.futures.as_completed(futures):
        ic(future.result())


if __name__ == "__main__":
    main()
