# Турист собирается в поход. Он сможет нести N кг вещей. 
# Но вещей, которые он запланировал уложить в рюкзак, 
# оказалось намного больше. 
# Нужно определить, какие вещи от наиболее тяжелых 
# к самым легким поместятся в рюкзак.

N = int(input("Введите сколько кг возьмем в поход: "))*1000
things = {'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300, 'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200, 'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 'жвачка': 10}
sortedthings = dict(sorted(things.items(), key = lambda x : -x[1]))
print(f"Это все вещи: {sortedthings}")
print('Можем взять с собой: ')
for k, v in sortedthings.items():
    if N > 0 and N >= v:
        N -= v
        print(k)