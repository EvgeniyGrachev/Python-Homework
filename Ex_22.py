# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

list_1 = list()
list_2 = list()
count_list_1 = int(input('Введите целое число, количество элементов списка 1: '))
count_list_2 = int(input('Введите целое число, количество элементов списка 2: '))

for i in range(count_list_1):
    num_1 = int(input('Введите целое число, знечение элемента списка 1: '))
    list_1.append(num_1)

for i in range(count_list_2):
    num_2 = int(input('Введите целое число, знечение элемента списка 2: '))
    list_2.append(num_2)

list_3 = list()
for i in range(count_list_1):
    if list_1[i] in list_2:
        list_3.append(list_1[i])

res = sorted(set(list_3))

print(res)