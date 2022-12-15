"""Напишите программу с классом Student, в котором есть четыре атрибута: firstName, lastName, groupNumber и age.
Установить им любые значения по умолчанию. Необходимо создать пять методов:
getFullName, getAge, getGroupNumber, setNameAge, setGroupNumber. Метод getFullName нужен для получения данных о полном
имени конкретного студента, метод getAge нужен для получения данных о возрасте конкретного студента,
метод GetGroupNumber нужен для получения данных о номере группы конкретного студента.
Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет изменить
номер группы установленный по умолчанию.
В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы."""

class Student:
    def __init__(self, firstName, lastName, groupNumber, age):
        self.firstName = firstName
        self.lastName = lastName
        self.groupNumber = groupNumber
        self.age = age

    def getFullName(self):
        print('Full name of this student is', self.firstName, self.lastName)

    def getAge(self):
        print(self.firstName, self.lastName, 'is', self.age, 'years old')

    def getGroupNumber(self):
        print(self.firstName, self.lastName, 'is studying in group number', self.groupNumber)

    def setNameAge(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

Pavel = Student('Pavel', 'Martinovich', 5, 23)
Angela = Student('Angela', 'Martinovich', 4, 22)
Vasilisa = Student('Vasilisa', 'Vasilevskaya', 3, 25)
Yuri = Student('Yuri', 'Martinovich', 1, 20)

Pavel.getFullName()
Pavel.getAge()
Pavel.getGroupNumber()
Angela.getFullName()
Angela.getAge()
Angela.getGroupNumber()
Yuri.getFullName()
Yuri.getAge()
Yuri.getGroupNumber()