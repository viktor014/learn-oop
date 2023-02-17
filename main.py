class Vector:
    "Класс для представления координат точек на плоскости "

    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x=0, y=0):
        print('Вызов __init__ для: ' + str(self))
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y

v = Vector(1,2)
res = v.get_coord()
print(res)
print((Vector.validate(105)))