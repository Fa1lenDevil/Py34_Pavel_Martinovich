#for i in range(0, 150, 2):
    #print(i)

#Text = "hello world"
#A = [10, 20, 30]
#B = (10, 20, 30)

#for i in A:
   # print(i)

#number = 0
#while True:
   # number += 1
    #if number % 2 == 0:
   #     continue
 #   print(number)

 #   if number == 99:
   #  print('end')


#Name = input('Введите ваше имя: ')
#Age = int(input('Введите ваш возраст: '))
#if Age < 18:
  #  print('Пошел вон, {}, ты малолетка'.format(Name))
#elif Age >= 18:
#    print('Привет, {}, тебе уже есть 18'.format(Name))

#number = [111, 215, 43, 4231, 26, 525, 127, 8532, 39, 410, 511, 12, 13, 14, 15]
#for i in range(1, (len(number)), 2):
  #  if i % 2 != 0:
  #      number[i] = 0
#print(number)

mylist = [50, -8, 90, 44, 71, 19, 42]
for i in range(len(mylist)):
    for m in range(len(mylist)):
        if mylist[i] < mylist[m]:
            mylist[i], mylist[m] = mylist[m], mylist[i]
print(mylist)

def summa(a, b):
    c = a + b
    return summa()




