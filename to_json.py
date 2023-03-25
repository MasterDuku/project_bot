import json

arr = []
# протестировать на различные входные данные, как читает при изменении кода как в комментиях внизу
with open('cenz.txt', 'r', encoding='utf-8') as file:
    for line in file:
       n = line.lower().split('\n')[0]
       if n != '':
           arr.append(n)

with open('cenz.json', 'w', encoding='utf-8') as file:
    json.dump(arr, file, ensure_ascii=False)


"""
https://www.youtube.com/watch?v=Lgm7pxlr7F0

Спасибо за видео. Всё очень здорово.
Маленькие ремарки:
9:33 - не надо писать "!=". Достаточно поставить двоеточие, т.к. пустое множество будет давать False:
if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()} \
            .intersection(set(json.load(open('cenz.json')))):

2:11 -  то же самое, не нужно пустую строку выставлять в сравнение. Пустая строка - это False
Я вообще так сделал:
with open('cenz.txt', encoding='utf-8') as r:
    ar = r.read().lower().split()
Хотя с точки зрения расходования памяти, могу быть не прав. Если кто шарит, поправьте.
"""