import peewee
from peewee import *
from datetime import date


db = MySQLDatabase("homework", user="root", password='Vfhnbyjdbx2000', port=3306, host="localhost")

class BaseModel(Model):
    class Meta:
        database = db

class Employees(BaseModel):
    firstName = peewee.CharField()
    lastName = peewee.CharField()
    working_from = peewee.DateField()
    department_id = peewee.CharField(2)


Employees.drop_table()
Employees.create_table()
Eve = Employees.create(firstName='Eve', lastName = 'Hoover', working_from=date(2020, 12, 2), department_id=20)
Zuzanna = Employees.create(firstName='Zuzanna', lastName='Lynch', working_from=date(2022, 1, 30), department_id=10)
Tyrone = Employees.create(firstName='Tyrone', lastName='Rocha', working_from=date(2021, 2, 20), department_id=20)
David = Employees.create(firstName='David', lastName='Brody', working_from=date(2021, 2, 2), department_id=17)
Nico = Employees.create(firstName='Nico', lastName='Lohard', working_from=date(2022, 11, 17), department_id=30)
David = Employees.create(firstName='David', lastName='Hobbs', working_from=date(2019, 6, 6), department_id=30)
d1 = date(2021,2,1)
d2 = date(2021,2,28)

for employee in Employees.select().where(Employees.department_id == 20):
    print(employee.firstName, employee.lastName)
for employee in Employees.select().where(Employees.department_id == 30):
    print(employee.firstName, employee.lastName)
for employee in Employees.select().where(Employees.firstName=='David'):
    print(employee.firstName,employee.lastName, employee.department_id)
for employee in Employees.select().where((Employees.working_from >= d1) & (Employees.working_from <= d2)):
    print(employee.firstName, employee.lastName)