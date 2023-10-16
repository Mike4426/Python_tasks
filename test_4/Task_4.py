'''Реализуйте контекст менеджер на основе класса, который создаёт временный файл с помощью 
библиотеки tempfile. В данном классе по мимо этого должны быть реализованы методы:
-repeat() - Дублирует текущее содержание файла и добавляет в конец файла
-write(msg) - Записывает текст в начало файла
-show() - Выводит содержимое файла в консоль
При окончании работы менеджера, должно быть напечатано количество символов в файле и закрыт временный файл.
'''

import tempfile

class Task_4:

    def __init__(self):

        self.temp = self._create_temp_file()

    #Создание временного файла
    def _create_temp_file(self):

        #Создание временного файла
        temp = tempfile.TemporaryFile()

        print('temp: {0}'.format(temp))
        print('temp.name: {0}'.format(temp.name))

        return temp

    #Дублирует текущее содержание файла и добавляет в конец файла
    def repeat(self):

        self.temp.seek(0)
        text = self.temp.read()

        self.temp.seek(0, 2)
        self.temp.write(text)
        
    #Записывает текст в начало файла
    def write(self, text: str):
        '''text - Текст для записи'''

        self.temp.seek(0)
        self.temp.write(text.encode('utf-8'))

    #Выводит содержимое файла в консоль
    def show(self):
        
        self.temp.seek(0)
        text = self.temp.read()
        print(text)
    
    #Закрыть файл
    def close_temp(self):

        #Подсчитаем количество файлов
        self.temp.seek(0)
        text = self.temp.read()
        print(f'Количество символов в файле: {len(text)}')

        self.temp.close()


if __name__ == '__main__':
    
    a = '123456789'
    task = Task_4()

    #Записываем в начало файла
    task.write(a)
    task.show()

    #Дублирование содерж. файла в конец файла
    task.repeat()
    task.show()

    #Закрытие
    task.close_temp()






