'''
На вход подаётся массив слов зависимых от регистра, для которых необходимо произвести фильтрацию на основании дублей слов,
если в списке найден дубль по регистру, то все подобные слова вне зависимости от регистра исключаются.
На выходе должны получить уникальный список слов в нижнем регистре.
 
words = ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']
# find_in_different_registers(words) -> ['папа', 'брат']
 
 
def find_in_different_registers(words):
  pass
 
 
print(find_in_different_registers(words))
'''


#Фильтрация на основе дублей слов (не зависимо от регистра)
def find_in_different_registers(words: list):
    '''words - список текстовых значений'''

    #Создаем копию списка words и возводим каждое слово к нижнему регистру
    list_words_lower = [i.lower() for i in words]

    #Проходим по каждому значению
    for i in range(len(words)):

        if words[i] in words[i+1:]:
            
            #Убираем из копии списка найденные значения (предварительно возведя их к нижнему регистру)
            list_words_lower = [i1 for i1 in list_words_lower if words[i].lower() != i1]
            #Убираем дубликаты
            list_words_lower = list(set(list_words_lower))

    return list_words_lower

if __name__ == '__main__':

    words = ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']


    print(find_in_different_registers(words))