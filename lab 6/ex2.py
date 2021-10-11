import math


class Vector(object):
    def __init__(self, str_inp):
        self.x, self.y, self.z = map(int, str_inp.split(','))

    def __add__(self, other):
        return Vector(str(self.x + other.x) + ',' + str(self.y + other.y) + ',' + str(self.z + other.z))

    def __sub__(self, other):
        return Vector(str(self.x - other.x) + ',' + str(self.y - other.y) + ',' + str(self.z - other.z))

    def __mul__(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __matmul__(self, other):
        return Vector(str(self.y * other.z - self.z * other.y) + ',' +
                      str(self.z * other.x - self.x * other.z) + ',' +
                      str(self.x * other.y - self.y * other.x))

    def __str__(self):
        return ','.join(map(str, (self.x, self.y, self.z)))

    @staticmethod
    def farthest_point(N, arr):
        my_arr = []
        for i in range(N):
            my_arr.append(Vector(arr[i]).__abs__())
        ind = my_arr.index(max(my_arr))
        return print(Vector(arr[ind]))

    @staticmethod
    def parallelogram(a, b):
        A = Vector(a)
        B = Vector(b)
        C = A @ B
        return C

    @staticmethod
    def parallelepiped(a, b, c):
        A = Vector(a)
        B = Vector(b)
        C = Vector(c)
        D = Vector.parallelogram(a, b)
        return D * C

    @staticmethod
    def triangle(N, arr):
        peri_arr = []
        area_arr = []
        peri = []
        area = []
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    a = Vector(arr[i])
                    b = Vector(arr[j])
                    c = Vector(arr[k])
                    m = a - b
                    n = a - c
                    p = b - c
                    if m @ n == Vector('0,0,0'):
                        continue
                    else:
                        peri_arr.append([arr[i], arr[j], arr[k]])
                        area_arr.append([arr[i], arr[j], arr[k]])
                        peri.append(abs(m) + abs(n) + abs(p))
                        area.append(1 / 2 * abs(m * n))
        max_peri = max(peri)
        print('The 3 vertices that create the triangle with the largest perimeter are: ')
        for x in peri_arr[peri.index(max_peri)]:
            print(x)
        print('The longest perimeter triangle is: ', max_peri)
        max_area = max(area)
        print('The 3 vertices that create the triangle with the largest area are: ')
        for x in peri_arr[area.index(max_area)]:
            print(x)
        print('The longest area triangle is: ', max_area)


N = int(input())
arr = []
center_point = Vector('0,0,0')
for i in range(N):
    a = input()
    arr.append(a)
    center_point = center_point + Vector(a)
'''
farthest point
'''
print('farthest point is : ', end=' ')
Vector.farthest_point(N, arr)

'''
center point 
'''


def center(center_point):
    return (center_point.x / N, center_point.y / N, center_point.z / N)


my_center_point = center(center_point)
print('center point is : ', end=' ')
print(my_center_point)

'''
area of parallelogram
'''
print('enter two vectors :')
a = input()
b = input()
print('area of parallelogram : ', abs(Vector.parallelogram(a, b)))

'''
volume of a parallelepiped
'''
print('enter three vectors :')
a = input()
b = input()
c = input()
print('area of parallelepiped : ', abs(Vector.parallelepiped(a, b, c)))

"""
longest perimeter triangle, longest area triangle
"""
Vector.triangle(N, arr)
