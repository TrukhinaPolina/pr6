a = {'Австралия': 'Канберра', 'Греция': 'Афины', 'Латвия': 'Рига', 'Лихтенштейн': 'Вадуц', 'Панама': 'Панама',
     'Эритрея': 'Асмэра', 'Япония': 'Токио'}
print(a)
b = input("введите страну ")
if b in a:
    c = a[b]
    print(c)
else:
    print("такой страны нет")
list_a = list(a.keys())
list_a.sort()
for i in list_a:
    print(i, " - ", a[i])
