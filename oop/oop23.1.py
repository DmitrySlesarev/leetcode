import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        logger.info(f"Geom init for {self.__class__}")
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2


    def get_coords(self):
        return (self.__x1, self.__y1)

class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill


if __name__ == "__main__":
    r = Rect(0, 0, 10, 20)
    r.get_coords()
    logging.info(r.__dict__)
