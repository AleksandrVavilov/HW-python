# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# Пример:
# list_1 = [2, 2, 2, 2, 5]
# k = 4
# count = 0
# for i in list_1:
#     if i == k:
#         count += 1
# print(count)

# list_1 = [2, 2, 2, 2, 5]
# k = 5
# count = list_1.count(k)
# print(count)

# Требуется найти в массиве list_1 самый близкий по значению 
# элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. 
# Если значение k совпадает с этим элементом - выведите его.
# Пример:
# list_1 = [1, 2, 3, 4, 5, 13, 3, 7, 9, 0]
# k = 6
# dif = abs(k - list_1[0])
# for i in list_1:
#     if abs(k - i) <= dif:
#         dif = abs(k - i)
#         result = i   
# print(result)
# МОЖНО ЗАМОРОЧИТЬСЯ С ПРОВЕРКОЙ НА ОТРИЦАТЕЛЬНОСТЬ ТОГО ИЛИ ИНОГО ЧИСЛА

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k 
# и выводит его. Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.
# count = 0
# k = 'ааа'
# points = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
# k = k.upper()
# for i in k:
#         for j in points:
#             if i in points[j]:
#                 count += j
# print(count)