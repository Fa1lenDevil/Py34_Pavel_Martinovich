'''Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
Создать файл и записать в него первые 2 строки и закрыть файл. Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки'''

'''name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = input('Введите возраст: ')
height = input('Введите рост: ')
with open('info.txt', 'wt') as file1:
    file1.write(name +'\n')
    file1.write(surname +'\n')
with open('info.txt', 'at') as file2:
    file2.write(age +'\n')
    file2.write(height + '\n')'''


'''Прочитать сохраненный джейсон-файл и записать данные на диск в csv-файл, первой строкой которого
 озаглавив каждый столбец и добавив новый столбец "телефон"'''


'''import json
import csv

with open('text.json') as j:
    data = json.loads(j.read())
    keys = list(data.keys())
    values = list(data.values())
    print(keys)
    print(values)
    with open("data.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(keys+['phone'])
        writer.writerow(values)'''


'''Создать словарь в качестве ключа которого будет 6-ти значное число(id), а в качестве значений кортеж состоящий 
из 2х элементов - имя(стр), возраст(инт). сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл'''

import json
dict = {
    "111111": "('Paul', 20)",
    "222222": "('Alex', 26)",
    "333333": "('Drake', 22)",
    "444444": "('Timati', 12)",
    "555555": "('Bilan', 41)",
    "666666": "('Basta', 43)"
}
dict_json = json.dumps(dict)

with open("dict_json.json", "w") as json_file:
    json_file.write(dict_json)
