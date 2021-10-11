import math

class Complex(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

    def __truediv__(self, other):
        r = float(other.real ** 2 + other.imag ** 2)
        return Complex((self.real * other.real + self.imag * other.imag) / r,
                       (self.imag * other.real - self.real * other.imag) / r)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '({}+{}j)'.format(self.real, self.imag)

    def __pow__(self, power):
        raise NotImplementedError \
            ('self**power is not yet impl. for Complex')


A = Complex(2, 5)
a = complex(2, 5)
B = Complex(3, 4)
b = complex(3, 4)
add_c = A + B
sub_c = A - B
mul_c = A * B
div_c = A / B
print(add_c)
print(a + b)
print(sub_c)
print(a - b)
print(mul_c)
print(a * b)
print(div_c)
print(a / b)
print(abs(A))
print(abs(complex(a)))
