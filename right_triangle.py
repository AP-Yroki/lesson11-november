class RightTriangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def increase_side(self, percent):
        self.base *= 1 + percent / 100
        self.height *= 1 + percent / 100

    def decrease_side(self, percent):
        self.base *= 1 - percent / 100
        self.height *= 1 - percent / 100

    def find_radius(self):
        h = (self.base ** 2 + self.height ** 2) ** 0.5
        radius = h / 2
        return radius

    def find_perimeter(self):
        h = (self.base ** 2 + self.height ** 2) ** 0.5
        perimeter = self.base + self.height + h
        return perimeter

    def find_angels(self):
        angle_A = self.degrees(self.arcsin(self.height / (self.base ** 2 + self.height ** 2) ** 0.5))
        angle_B = self.degrees(self.arcsin(self.base / (self.base**2 + self.height**2)**0.5))
        angle_C = 90
        return angle_A, angle_B, angle_C

    def arcsin(self, x):
        angle = x
        power = x
        n = 1
        while n < 50:
            power *= x * x * (2 * n - 1) * (2 * n - 1) / ((2 * n) * (2 * n + 1))
            angle += power / (2 * n + 1)
            n += 1
        return angle

    def degrees(self, radians):
        return radians * 180 / 3.141592653589793


triangle1 = RightTriangle(3, 4)

print(triangle1.find_perimeter())
print(triangle1.find_angels())
print(triangle1.find_radius())
