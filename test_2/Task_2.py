'''Реализовать декоратор, который позволяет кешировать результат вызова функции и выводит время выполнения. 
Для вывода времени выполнения необходимо использовать модуль logging. Также декоратор должен принимать необязательный 
аргумент, который отвечает за то через сколько вызовов вызываемая функция будет заново исполнена и значение в кеше 
обновиться, значение по умолчанию для данного аргумента 3.'''

from random import randint
import logging
import time
from functools import lru_cache


#Декоратор высчитывания времени выполения
def execution_time(func, doorstep = 3):
    '''doorstep - (int) количество выполнений функций после которой кэш будет обновлен'''

    def run(num):
        
        #Проверяет соответствие количества выполнений функций (в случае не выполнения обновить хэш)
        if func.cache_info()[0] == (doorstep-1):
            func.cache_clear()

        logging.basicConfig(level=logging.INFO)

        #Замеры времени выполнения
        time_start = time.time()
        out = func(num)
        time_finish = time.time() - time_start

        #Вывод информации о времени выполнения
        logging.info(f'Время выполнения функции: {time_finish} сек.')
        return out

    return run


@execution_time
@lru_cache
#Генерация список случайных значений от 0 до 100
def random_number_generation(number: int):
    '''number - Длина списка'''

    list_rand = [randint(0, 100) for i in range(number)]

    return list_rand


if __name__ == '__main__':

    #Проверка всех значений
    for i in range(10):
        print(random_number_generation(100_000)[0:3])









