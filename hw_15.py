"""создайте список объектов разных типов, для каждого объекта в цикле выведите:
* порядковый номер начиная с единицы
* значение
* адрес в памяти
* размер в памяти
* результат проверки на целое число если он положительный
* результат проверки на строку если он положительный
******** решил логировать только целые положительные числа и строки ***********
"""
import sys
import logging

data = [2, "hi", 3.14, 8, "hello", 2]
logging.basicConfig(format="%(levelname)s (%(asctime)s) [%(filename)s].%(name)s: %(message)s ", encoding="utf8", filemode="w",
    filename="logs/log_info.log", level=logging.INFO)
logger = logging.getLogger("user")
i = 0
for elem in data:
    logger.debug(elem)
    i += 1
    logger.debug(f"порядковый номер: {i}")
    logger.debug(f"адрес в памяти: {id(elem)}")
    logger.debug(f"размер в памяти: {sys.getsizeof(elem)}")
    logger.debug(f"хэш объекта: {hash(elem)}")
    if isinstance(elem, (int)):
        if elem > 0:
            logger.info(f"{elem} -это целое положительное число\nпорядковый номер: {i}\nадрес в памяти: {id(elem)}\n"
                    f"размер в памяти: {sys.getsizeof(elem)}\nхэш объекта: {hash(elem)}\n")

    if isinstance(elem, str):
        logger.info(f"{elem} - это строка \nпорядковый номер: {i}\nадрес в памяти: {id(elem)}\n"
                        f"размер в памяти: {sys.getsizeof(elem)}\nхэш объекта: {hash(elem)}\n")
