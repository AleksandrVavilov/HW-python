# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. 
# ! Писать input() не надо
# var1 = '5 4' 
# var2 = '1 3 5 7 9' 
# var3 = '2 2 3 4 5' 
# var2 = set(var2.split())
# var3 = set(var3.split())
# # var4 = var2.intersection(var3)
# print(*sorted(var2 & var3))


# В фермерском хозяйстве в Карелии выращивают чернику. 
# Черника растет на круглой грядке, и кусты черники высажены по окружности грядки. 
# Каждый куст черники имеет урожайность, 
# которая соответствует количеству ягод на этом кусте.
# Урожайность черничных кустов представлена в виде списка arr, 
# где arr[i] - это урожайность (количество ягод) i-го куста.
# В фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. 
# Собирающий модуль находится перед определенным кустом, и он может выбирать, 
# с какого куста начать сбор ягод.
# Ваша задача - написать программу, которая определит максимальное число ягод, 
# которое может собрать один собирающий модуль за один заход, 
# находясь перед некоторым кустом грядки.
# Входные данные:
# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - 
# урожайность i-го куста черники. Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число - максимальное количество ягод, 
# которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.
# Пример использования На входе:
# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# На выходе:
# 19



arr = [15, 21, 1, 4, 9, 2, 7, 3, 17, 21]
sum = 0 
i = 0
while i < len(arr):
    if sum < arr[i-2] + arr[i-1] + arr[i]:
        sum = arr[i-2] + arr[i-1] + arr[i]
    i += 1
print(sum)










# arr = [15, 21, 1, 4, 9, 2, 7, 3, 17, 21]
# sum = 0 
# for i in range(len(arr)):
#     if sum < arr[i-1] + arr[i] + arr[(i+1)%len(arr)]: #хитро взяли первый элемент когда список закончился
#         sum = arr[i-1] + arr[i] + arr[(i+1)%len(arr)]
# print(sum)