import logging
from typing import Optional, Dict, Any, List

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = "https://jsonplaceholder.typicode.com/users"


def get_users(
        url: str = URL,
        name: Optional[str] = None,
        email: Optional[str] = None,
        city: Optional[str] = None
) -> Optional[List[Dict[str, Any]]]:
    """
    Fetch users from API with optional filters

    Args:
        url: API endpoint URL
        name: Filter by name (partial match)
        email: Filter by email (exact match)
        city: Filter by city (requires post-processing)

    Returns:
        List of user dictionaries or None if error occurs
    """
    params: Dict[str, str] = {}
    if name:
        params["name"] = name
    if email:
        params["email"] = email

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        users = response.json()

        if city and users:
            users = [
                user for user in users
                if user.get('address', {}).get('city', '').lower() == city.lower()
            ]

        return users

    except requests.exceptions.Timeout:
        logger.error(f"Request timed out for URL: {url}")
        return None
    except requests.exceptions.ConnectionError:
        logger.error(f"Connection error for URL: {url}")
        return None
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error {e.response.status_code}: {e.response.reason}")
        return None
    except requests.exceptions.JSONDecodeError:
        logger.error("Response contained invalid JSON")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return None


if __name__ == "__main__":
    users1 = get_users(name="Leanne")
    print(f"{users1=}")

    users2 = get_users(city="South Christy")
    print(f"{users2=}")

    users3 = get_users(email="Nathan@yesenia.net")
    print(f"{users3=}")
