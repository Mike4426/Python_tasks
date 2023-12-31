'''
Реализовать решение для генерации случайных данных в формат csv. 
На входе:
N - количество строк необходимое для генерации
header - словарь ключом которого является название колонки, а значением один из типов: int, str или bool. 
Файл обязательно должен содержать заголовок.

Кол-во строк ограничено: 109
Для генерации типа str длина текста не должна превышать > 100.
Для генерации типа int: диапазон значений от 0 до 100, целочисленные.
'''

from random import randint, random
import numpy as np

class Data_generation:

    #Декоратор замера времения выполнения (не обязательное)
    def decoration(func):

        def run(*arg):
            import time

            start = time.time()
            out = func(*arg)
            print(f'{func.__name__}: {round(time.time() - start, 3)}')
            return out

        return run
    
    @decoration
    def __init__(self, N: int, header: dict):
        '''N - количество строк необходимое для генерации\n
        header - словарь ключом которого является название колонки, а значением один из типов: int, str или bool'''

        self.N = N
        self.header = header
        self.name_file = 'test.csv' #Название csv файла

        #Проверка ограничения на количества строк
        if self.N > 1_000_000_000: self.N = 1_000_000_000

        #Проверка что есть хоть 1 заголовок
        if len(self.header.keys()) > 0: 
            
            #Генерация рандомных значений
            self.csv = self.generation_csv()
            #Запись в файл
            self.write_file_csv()
    
    #Генерация int
    def generation_number(self, count_num: int):
        '''count_num - Количество значений'''

        num = list(np.random.randint(0, 100, count_num))
        return num
    
    #Генерация значений str
    def generation_str(self, count_str: int):
        '''count_str - Количество значений'''

        #Выставляем длину строк
        len_str = randint(10, 100)

        #Загружаем список нашего словаря (который находится в директории)
        with open('test_7/text_line.txt', 'r', encoding='utf-8') as f:
            list_data = f.read()
        list_data = list_data.split('\n')

        #Генерируем случайный текст
        list_text = [list_data[np.random.randint(0, len(list_data)-1)] for i in range(count_str)]


        return list_text
    
    #Генерация значений bool
    def generation_bool(self, count_bool: int):
        '''count_bool - Количество значений'''

        list_bool = [bool(randint(0, 1)) for i in range(count_bool)]
        return list_bool

    #Генерация значений csv
    def generation_csv(self):
        
        #Создаем словарь
        out = {}
        #Конечный текст
        text_out = ''

        #Добавляем значения в словарь
        for i in self.header.keys():

            if self.header[i] == 'int':
                out[i] = self.generation_number(self.N)

            elif self.header[i] == 'str':
                out[i] = self.generation_str(self.N)

            else:
                out[i] = self.generation_bool(self.N)

        #Добавление строки
        for i in range(self.N):

            _ = []

            #Проходим по колонкам (добавляем значения к строке) 
            _ = [str(out[i1][i]) for i1 in self.header.keys()]
            
            _ = ','.join(_)
            text_out = text_out + _ + '\n'
        
        #Добавляем заголовки
        _ = ','.join(out.keys())
        text_out = _ + '\n' + text_out

        return text_out

    #Создаем/записываем файл csv
    def write_file_csv(self):

        with open(self.name_file, 'w') as f:
            f.write(self.csv)


if __name__ == '__main__':
    
    Data_generation(20_000, {'Название_1': 'int', 'Название_2': 'bool', 'Название_3': 'str', 'Название_4': 'str'})
    
    
    
