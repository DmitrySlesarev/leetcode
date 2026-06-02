import logging
import threading

import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


def download_file(url, filename):
    logger.info(f"Downloading {filename}")
    try:
        result = requests.get(url, timeout=10)
        result.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(result.content)
        logger.info(f"Successfully finished {filename}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to download {filename} due to {e}")
        return False
    return True


urls = [
    ("https://httpbin.org/image/jpeg", "test1.jpg"),
    ("https://httpbin.org/image/png", "test2.png"),
    ("https://www.python.org/static/img/python-logo.png", "python_logo.png")
]


def main():
    threads = []

    for url, filename in urls:
        t = threading.Thread(target=download_file, args=(url, filename))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    logger.info("All threads have finished execution")


if __name__ == "__main__":
    main()
