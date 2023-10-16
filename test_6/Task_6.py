'''Реализовать скрипт, который позволяет валидировать csv файл на корректность его заполнения. Валидация должна включать в 
себя такие параметры, как:
•	Отсутствие/Присутствие заголовка: по умолчанию присутствует
•	Выбор разделителя: по умолчанию запятая

Скрипт должен поддерживать передачу параметров через командную строку с использованием библиотеки argparse. 

(Путь к файлу обяз., остальные необязательные). Должен поддерживать вызов --help для описания передаваемых параметров.

Вызов скрипта является корректным, если он завершается со статусом 0, в случае нахождении ошибки в файле, должна быть 
выведена проблема и завершён со статусом 1
'''
import argparse


#Валидация csv файлов на корректность его заполнения
class Validation_csv:

    
    def validation(self, path:str, title = True, separator = ','):
        '''path - Путь к файлу csv (str)\n
        title: bool - Отсутствие/Присутствие заголовка: по умолчанию присутствует\n
        separator: str - Какой используется разделитель'''
        
        try:
            #Чтение файла
            with open(path, 'r') as f:
                text_file = f.read()
            print('Ошибок в чтении файла не обнаружено')
            
            #Делим полученный текст на строки
            text_file_row = text_file.split('\n')

            #Удаляем последнюю пустую строку (если она есть)
            if text_file_row[-1] == '':
                del text_file_row[-1]

            #Делим по разделителю
            text_file = [i.split(separator) for i in text_file_row]
            print('Ошибок в обработке файлов не обнаружено')
            
            #Проверяем на корректность количества ячеек в каждой строке
            if title == True:

                #Узнаем сколько максимальное количество колонок доступно
                max_column = len(text_file[0])

                #Заносим в список индекс строки, размер которой не совпадает с заголовком
                row_error = [i for i in range(len(text_file_row)) if max_column != len(text_file[i])]

            else:
                row_error = []

            
            #Выводим сообщение что все ок! если нет то выводим номера строк которые не совпадают
            if len(row_error) > 0:
                raise Exception()
            else:
                print('Ошибок по количеству ячеек не обнаружено.')

        except FileNotFoundError:
            print('--ОШИБКА! Возможно ошибка в названии файла. Файл не обнаружен')
            print('Завершено со статусом 1')
            return 1
        except Exception:
            print(f'--ОШИБКА! Количество ячеек не совпадает с заголовком в индексах данных строк: {row_error}')
            print('Завершено со статусом 1')
            return 1
        else:
            print('Общих ошибок по файлу не обнаружено')
            print('Завершено со статусом 0')
            return 0

        
if __name__ == '__main__':
    
    val = Validation_csv()
    pars = argparse.ArgumentParser()

    #Добавляем аргументы
    pars.add_argument('path', type=str, help='Путь к к данным csv (str)')
    pars.add_argument('-t', '-title', type=str, help='Наличие заголовка в csv (bool)', default = True)
    pars.add_argument('-s' ,'-separator', type=str, help='Знак разделитель (str)', default = ',')

    #Получаем аргументы
    arg = pars.parse_args()

    #Форматируем текстовое выражение в bool
    if arg.t in ('False', 'false'): arg.t = False
    elif arg.t in ('True', 'true'): arg.t = True

    val.validation(arg.path, arg.t, arg.s)
    
    #test_6/1.csv