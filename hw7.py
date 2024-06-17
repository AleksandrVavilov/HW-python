# Напишите функцию print_operation_table(operation, num_rows, num_columns), 
# которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. 
# По умолчанию номер столбца и строки = 9.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
# Пример
# На входе:
# print_operation_table(lambda x, y: x * y, 3, 3)
# На выходе:
# 1 2 3
# 2 4 6 
# 3 6 9
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
#     for i in range(1, num_rows+1):
#         row = []
#         for j in range(1, num_columns+1):
#             row.append(str(operation(i, j)))
#         print("\t".join(row))
# # можно слепить методом join из списка строку
# print_operation_table(lambda x, y: x * y, 9, 9)



# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух передаст вам автоматически 
# в переменную stroka в виде строки. 
# В ответе напишите Парам пам-пам, если с ритмом все в порядке 
# и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится 
# и необходимо вывести: Количество фраз должно быть больше одной!.
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# stroka = stroka.split()
# count_vowels = list(map(lambda x: sum(map(x.count, 'уеёыаоэяию')), stroka)) 
# #перебираем последовательно строки, в них перебираем буквы и считаем кол-во гласных
# if len(stroka)< 2:
#     print("Количество фраз должно быть больше одной!")
# elif max(count_vowels) == min(count_vowels):
#      print("Парам пам-пам")
# else:
#     print("Пам парам")


stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
def count_vowels(word):
    vowels = "аеёиоуыэюя"
    return sum(1 for char in word if char in vowels)
def check_rhythm(stroka):
    phrases = stroka.split()

    if len(phrases) < 2:
        return "Количество фраз должно быть больше одной!"

    syllables_count = [sum(count_vowels(word) for word in phrase) for phrase in phrases]
    if all(count == syllables_count[0] for count in syllables_count):
        return "Парам пам-пам"
    else:
        return "Пам парам"

print(check_rhythm(stroka))