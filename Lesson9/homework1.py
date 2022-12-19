import json
with open('file.json') as file:
    data = json.loads(file.read())

from dataclasses import dataclass
@dataclass
class DataBrand:
    brand: str
    mark: str
    max_speed: int
    horse_power: int

class Brand(DataBrand):
    @property
    def brand(self):
        print(self.brand)
        return self.brand
    @property
    def mark(self):
        print(self.mark)
        return self.mark
    @property
    def max_speed(self):
        print(self.max_speed)
        return self.max_speed
    @property
    def horse_power(self):
        print(self.horse_power)
        return self.horse_power

newClass = type("newClass", (DataBrand, ), data)
newObject = newClass
brand = newObject.brand
mark = newObject.mark
max_speed = newObject.max_speed
horse_power = newObject.horse_power
print(brand, mark, max_speed, horse_power)






