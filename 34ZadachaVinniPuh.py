"""Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку 
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять 
из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются 
друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе 
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не 
в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
**Вывод:** Парам пам-пам  """


"""на вход функции подаём два параметра - строку-стих и гласные букв. строку считываем через сплит,
 разбивается на три слова, прогоняем каждое слово через цикл for в 24 строке и для каждого символа в слове
  сравниваем с нашим списком гласных букв, если совпало, то прибаляем в sum_slom, и это каждое значение, добавляем в 
     конец spis. после возвращаем через return сравнение длины spis и счётчика count, и если одинаковое количество, то 
      возвращаем фразу "парам пам пам", если иначе, то фразу "пам парам"    """
def VinnyIkrichalki(s,g):
    s = s.split()
    spis = []
    for word in s:
        sum_slow = 0
        for i in word:
            if i in g:
                sum_slow += 1
        spis.append(sum_slow)
        print(spis.count(spis[0]))
    return len(spis) == spis.count(spis[0])


krichalka = "пара-ра-рам рам-пам-папам па-ра-па-да"
glasnie = "ауоыиэяюёе"
if VinnyIkrichalki(krichalka,glasnie):
    print('Парам пам пам')
else:
    print('парам пам')
            
