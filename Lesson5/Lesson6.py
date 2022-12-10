'''text = b'r\xc3\xa9sum\xc3\xa9'
text = text.decode()
print(text)
text = text.encode('latin1')
print(text)
text = text.decode('latin1')
print(text)'''

A = input('Введите имя: ')
B = input('Введите фамилию: ')
C = input('Введите возраст: ')
D = input('Введите рост: ')

with open('text.txt', 'w') as f:
    #f.write(A+'\n')
    #f.write(B+'\n')
    print(A, file=f)
    print(B, file=f)
with open('text.txt', 'a') as f:
    print(C, file=f)
    print(D, file=f)
   # f.write(C+'\n')
   # f.write(D+'\n')