"""Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 
"""
a = int(input('введите число А:'))
b = int(input('введите целое число, степень возведения В:'))
def numbstepen(a,b):
    if b == 0: # исходя из условий, что степень должна быть целой, выход из рекурсии при b = 0
        return 1
    return a * numbstepen(a,b-1)

print(numbstepen(a,b))


  