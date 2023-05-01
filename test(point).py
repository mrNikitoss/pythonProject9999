class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    """ Расстояние между двумя точками """
    import math
    return math.sqrt(abs(p1.x-p2.x)^2+abs(p1.y-p2.y)^2)


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()
# TODO: your code here...
print("Расстояние между точками = ", distance(point1,point2))