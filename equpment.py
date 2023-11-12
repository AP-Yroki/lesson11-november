class Equipment:

    def __init__(self, name, make, year):
        self.name = name  # производитель
        self.make = make  # модель
        self.year = year  # год выпуска

    def action(self):
        return 'Не опредлена'

    def __le__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError
        return self.year <= other.year

    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}'

class Printer(Equipment):

    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'Печатает с компа на листочек'

    def __str__(self):
        return f'{self.series}, {self.name}, {self.make}, {self.year}'

class Scaner(Equipment):

    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'сканирует в комп'

class Xerox(Equipment):

    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'копирует и печатает на листочек'

def alitems(sklad):
    for item in sklad:
        print(item)

def get_items(sklad, ename):
    for item in sklad:
        if isinstance(item, ename):
            print(item)

sklad = []
e = Equipment('frog', 'x', 2000)
print(e)
s = Scaner('dog', 'bob', 1976)
print(s)
p = Printer(15, 'yellow', 'hello', 2015)
print(p)
x = Xerox('test', 'bib', 'bob')
print(x)
print(e <= s <= p)
sklad.append(x)
sklad.append(s)

get_items(sklad, Equipment)







