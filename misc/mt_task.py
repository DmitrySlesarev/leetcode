import time
import sqlite3
import logging
import requests
from multiprocessing import Pool, cpu_count
from multiprocessing.pool import ThreadPool
from functools import partial

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_database():
    """Initialize database once at startup"""
    conn = sqlite3.connect('starwarscharacters.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS characters
                    (name text,
                    height text,
                    mass text,
                    haircolor text,
                    skincolor text,
                    eyecolor text,
                    birthyear text,
                    gender text)''')
    conn.commit()
    conn.close()


def get_peoples_data(conn_params, number: int) -> None:
    """Fetch and insert character data"""
    url = f"https://swapi.dev/api/people/{number}/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        database_manage(conn_params, data)
    except requests.RequestException as e:
        logger.error(f"Failed to fetch character {number}: {e}")
    except Exception as e:
        logger.error(f"Error processing character {number}: {e}")


def database_manage(conn_params, data: dict) -> None:
    """Insert data using connection parameters"""
    conn = None
    try:
        conn = sqlite3.connect('starwarscharacters.db', timeout=10)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS characters
                        (name text,
                        height text,
                        mass text,
                        haircolor text,
                        skincolor text,
                        eyecolor text,
                        birthyear text,
                        gender text)''')

        cursor.execute('''INSERT OR REPLACE INTO characters 
                        (name, height, mass, haircolor, skincolor, eyecolor, birthyear, gender)
                        VALUES (?,?,?,?,?,?,?,?)''',
                       (data.get('name', 'unknown'),
                        data.get('height', 'unknown'),
                        data.get('mass', 'unknown'),
                        data.get('hair_color', 'unknown'),
                        data.get('skin_color', 'unknown'),
                        data.get('eye_color', 'unknown'),
                        data.get('birth_year', 'unknown'),
                        data.get('gender', 'unknown')))

        conn.commit()
    except sqlite3.OperationalError as e:
        logger.error(f"Database error: {e}")
    finally:
        if conn:
            conn.close()


def sequential_approach():
    """Sequential execution - one request at a time"""
    start = time.time()
    input_value = [i for i in range(1, 21)]

    # Reinitialize database for clean comparison
    init_database()

    for inp in input_value:
        get_peoples_data(None, inp)
    end = time.time()
    logger.info(f'Time taken in seconds for sequential - {end - start:.2f}')


def high_load_map():
    """Process Pool approach (CPU-bound multiprocessing)"""
    start = time.time()
    input_value = [i for i in range(1, 21)]

    # Reinitialize database for clean comparison
    init_database()

    with Pool(processes=cpu_count()) as pool:
        pool.map(partial(get_peoples_data, None), input_value)

    end = time.time()
    logger.info(f'Time taken in seconds for Process Pool - {end - start:.2f}')


def execution_with_threadpool():
    """Thread Pool approach (I/O-bound threading)"""
    start = time.time()
    input_value = [i for i in range(1, 21)]

    # Reinitialize database for clean comparison
    init_database()

    with ThreadPool(processes=cpu_count() * 5) as pool:
        pool.map(partial(get_peoples_data, None), input_value)

    end = time.time()
    logger.info(f"Time taken in seconds for Thread Pool - {end - start:.2f}")


def cleanup_database():
    """Optional: Drop the database table for clean testing"""
    try:
        conn = sqlite3.connect('starwarscharacters.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS characters")
        conn.commit()
        conn.close()
        logger.info("Database cleaned up")
    except Exception as e:
        logger.error(f"Cleanup error: {e}")


if __name__ == "__main__":
    logger.info("=" * 50)
    logger.info("Starting performance comparison (20 Star Wars characters)")
    logger.info("=" * 50)

    # Run each approach separately for fair comparison
    # Uncomment the one you want to test

    sequential_approach()
    high_load_map()
    execution_with_threadpool()

    # Optional: Clean up between runs
    # cleanup_database()

