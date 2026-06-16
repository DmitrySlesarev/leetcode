import asyncio
import logging
from typing import Union

import aiofiles
import aiohttp


class CoroutineAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        try:
            current_task = asyncio.current_task()
            coro_name = current_task.get_name() if current_task else "main"
        except RuntimeError:
            coro_name = "main"

        if 'extra' not in kwargs:
            kwargs['extra'] = {}
        kwargs['extra']['coroutine'] = coro_name

        return msg, kwargs

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(coroutine)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)

base_logger = logging.getLogger(__name__)
logger: CoroutineAdapter = CoroutineAdapter(base_logger, {})


async def download_file(session, url, filename):
    """Download a file asynchronously"""
    logger.info(f"Downloading {url} as {filename}")

    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
            response.raise_for_status()

            async with aiofiles.open(filename, 'wb') as f:
                await f.write(await response.read())

    except aiohttp.ClientError as e:
        logger.error(f"Failed to download {filename} due to {e}")
        return False
    except asyncio.TimeoutError:
        logger.error(f"Timeout downloading {filename}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error downloading {filename}: {e}")
        return False

    logger.info(f"{filename} downloaded successfully")
    return True


async def main():
    logger.info("Start script")

    urls = [
        ('https://httpbin.org/image/jpeg', 'image1.jpg'),
        ('https://httpbin.org/image/jpeg', 'image2.jpg'),
        ('https://httpbin.org/image/jpeg', 'image3.jpg')
    ]

    async with aiohttp.ClientSession() as session:
        tasks = []
        for idx, (url, filename) in enumerate(urls):
            # Give each task a name for logging
            task = asyncio.create_task(
                download_file(session, url, filename),
                name=f"Download-{idx}"
            )
            tasks.append(task)

        results = await asyncio.gather(*tasks, return_exceptions=True)

        success_count = sum(1 for r in results if r is True)
        failure_count = len(results) - success_count

        logger.info(f"Downloads completed: {success_count} succeeded, "
                    f"{failure_count} failed")

        logger.info("Finish script")


if __name__ == "__main__":
    asyncio.run(main())
