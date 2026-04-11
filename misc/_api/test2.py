import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def create_user(title, body, user_id):

    data = {
        "title": title,
        "body": body,
        "user_id": user_id
    }

    headers = {
        "Content-type": "application/json"
    }

    try:
        response = requests.post(url=BASE_URL, json=data, headers=headers,timeout=10)
        response.raise_for_status()

        users = response.json()

        logger.info("Request is successful")
        return users

    except requests.exceptions.ConnectTimeout:
        logger.error("Connection timed out")
        return None
    except requests.exceptions.ConnectionError:
        logger.error("Connection broke")
        return None
    except requests.exceptions.JSONDecodeError:
        logger.error("JSON decoding broke")
        return None
    except Exception as e:
        logger.error(f"Unknown error {e}")
        return None


if __name__ == "__main__":
    print(create_user("Hello", "API learning", 1))