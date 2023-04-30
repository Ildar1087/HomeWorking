"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число 
X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число 
N – количество элементов в массиве. В последующих  строках записаны N целых 
чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1    """

n = int(input('Введите количество элементов массива А: '))
a_enter = input('Введите через пробел элементы: ').split()
a_num = list(map(int, a_enter))
if len(a_enter) != n: # проверка на точность ввода
    print('количество введенных элементов не соответстует заявленному!!!')
else:
    X = int(input('введите элемент "Х" для поиска: '))
    count = 0
    for i in range(n): 
        if a_num[i] == X: # перебираем массив с поиском искомого числа
            count += 1
    print(f'Число {X} встретилось в списке A {count} раз')

