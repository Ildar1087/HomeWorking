"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
не превосходящие числа N.

Пример
Ввод: 17 -> Вывод: 1, 2, 4, 8, 16    """

n = int(input('введите число N: '))
stop = 0 
p = 2 # шаг степени 2
for i in range(n): # выполняем до числа n
    if stop != 1: # пока не равно 1 выполняется условие
        p = p ** i # возводим i в степень двойки
        if p <= n:  # если р меньше или равно n, выполняется 
            print(p, end=' ') # выводим значения р, через пробел используя end=' '
            p = 2 # переприсваием значение р = 2 для повторения итераций
        else:
            stop = 1 # оставновка от зацикливания
    else:
        i = n  # оставновка от зацикливания

   

