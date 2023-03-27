# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exp(n, d):
    if d == 0:
        return 1
    else:
        return exp(n, d - 1) * n

number = int(input('Введите целое положительное число A: '))
degree = int(input('Введите степень B: '))

print(f"A = {number}; B = {degree} -> {exp(number, degree)}")