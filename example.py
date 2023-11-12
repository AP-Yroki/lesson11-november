class Clock:
    __DAV = 86400

    def __init__(self, seconds : int):
        if not isinstance(seconds, int):
            raise TypeError('Введите целое число')
        self.seconds = seconds % self.__DAV

    def get_time(self):
        s = self.seconds % 60
        m = self.seconds // 60 % 60
        h = self.seconds // 3600 % 24
        return f'{h} : {m} : {s}'

    def __eq__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError ('Нужно ввести целое число')
        p = 5**8
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc

    def __lt__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Type Error')
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc

    def __le__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Type Error')
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds <= sc

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Не можем сложить!!!')

        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds + sc)

    def __mul__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Не можем сложить!!!')

        return Clock(self.seconds * other)
cl = Clock(86401)
cl2 = Clock(54)
cl3 = Clock(155)
print(cl.get_time())
cl = cl * 3
print(cl.get_time())




