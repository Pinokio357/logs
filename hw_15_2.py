"""решил доработать предыдущую задачу и записываль целые положительные числа и строки в разные Лог-файлы"""
import logging
import sys


logger = logging.getLogger("not_important")
formatter = logging.Formatter("%(levelname)s (%(asctime)s) [%(filename)s].%(name)s: %(message)s")

logger_1 = logging.getLogger("numbers")
handler_1 = logging.FileHandler(filename="logs/numbers.log", mode="w", encoding="utf8")
handler_1.setFormatter(formatter)
logger_1.addHandler(handler_1)
logger_1.setLevel(logging.INFO)

logger_2 = logging.getLogger("strings")
handler_2 = logging.FileHandler(filename="logs/strings.log", mode="w", encoding="utf8")
handler_2.setFormatter(formatter)
logger_2.addHandler(handler_2)
logger_2.setLevel(logging.INFO)



data = [2, "hi", 3.14, 8, "hello", 2, -8, True]

i = 0
for elem in data:
    logger.debug(f"{elem}")
    i += 1
    logger.debug(f"порядковый номер: {i}")
    logger.debug(f"адрес в памяти: {id(elem)}")
    logger.debug(f"размер в памяти: {sys.getsizeof(elem)}")
    logger.debug(f"хэш объекта: {hash(elem)}\n")
    if isinstance(elem, (int)):
        if elem > 0:
            logger_1.info(f"{elem} -это целое положительное число\nпорядковый номер: {i}\nадрес в памяти: {id(elem)}\n"
                    f"размер в памяти: {sys.getsizeof(elem)}\nхэш объекта: {hash(elem)}\n")

    if isinstance(elem, str):
        logger_2.info(f"{elem} - это строка \nпорядковый номер: {i}\nадрес в памяти: {id(elem)}\n"
                        f"размер в памяти: {sys.getsizeof(elem)}\nхэш объекта: {hash(elem)}\n")