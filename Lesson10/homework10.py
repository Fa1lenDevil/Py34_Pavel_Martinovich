def fib(n):
    def fibIter(a, b, count):
        if count == 0:
            return b
        else:
            return fibIter(a+b, a, count-1)
    return fibIter(1, 0, n)
print(fib(100))



def fib(n):
    a, b = 1, 1
    for c in range(n):
        yield a
        a, b = b, a + b
print(list(fib(100)))



import re

userinput = input('Введите время: ')
pattern = ("^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$")
result = re.match(pattern, userinput) is not None
print(result)



import re

userindex = input('Введите почтовый индекс: ')
indexpass = re.match(r'\d{6}', userindex) is not None
if indexpass == True:
    brestres = re.match(r'224', userindex) is not None
    vitebskres = re.match(r'210', userindex) is not None
    gomelres = re.match(r'246', userindex) is not None
    grodnores = re.match(r'230', userindex) is not None
    mogilevres = re.match(r'212', userindex) is not None
    minskres = re.match(r'220', userindex) is not None
    if brestres == True:
        print('Брест')
    elif vitebskres == True:
        print('Витебск')
    elif gomelres == True:
        print('Гомель')
    elif grodnores == True:
        print('Гродно')
    elif mogilevres == True:
        print('Могилев')
    elif minskres == True:
        print('Минск')
    else:
        print('Такого индекса не существует')
else:
    print('Такого индекса не существует')
