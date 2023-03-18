# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import array as arr 

array = arr.array('i',[])
count_array = int(input('Введите количество элементов массива: '))

for i in range(count_array):
    num = int(input('Введите целое число, знечение элемента массива: '))
    array.append(num)

number = int(input('Введите целое: '))

min = number
result = array[0]
for i in array:
    if abs(i - number) < min:
        min = abs(i - number)
        result = i

print(f"{result} - ближайший элемент массива")