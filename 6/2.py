a = {'Р': '1', 'Т': '1', 'И': '1', 'В': '1', 'Н': '1', 'С': '1', 'Е': '1', 'А': '1', 'О': '1', 'У': '2', 'Л': '2',
     'П': '2', 'М': '2', 'К': '2', 'Д': '2', 'Ь': '3', 'Б': '3', 'Я': '3', 'Ё': '3', 'Г': '3', 'Ы': '4', 'Й': '4',
     'Ч': '5', 'Х': '5', 'Ж': '5', 'Ц': '5', 'З': '5', 'Ш': '8', 'Э': '8', 'Ю': '8', 'Ф': '10', 'Щ': '10', 'Ъ': '10'}
word = list(input("введите слово - ").upper())
k = 0
for x in word:
    for y in a:
        if x == y:
            b = a[y]
            k = int(b) + k

print(k)
