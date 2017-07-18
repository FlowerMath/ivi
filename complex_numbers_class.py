class ComplexNumber:
    def __init__(self, r_part, im_part):
        self.real = r_part
        self.im = im_part

    def __eq__(self, other):
        if self.real == other.real and self.im == other.im:
            return True
        else:
            return False

    def printing(self):
        print(self.real, '+', self.im, 'i')

    def module2(self):
        return self.real ** 2 + self.im ** 2

    def plus(self, other):
        return ComplexNumber(self.real + other.real, self.im + other.im)

    def adj(self):
        return ComplexNumber(self.real, -self.im)

    def minus(self, other):
        return ComplexNumber(self.real - other.real, self.im - other.im)

    def multi(self, other):
        return ComplexNumber(self.real * other.real - other.im * self.im,
                             self.im * other.real + self.real * other.im)

    def division(self, other):
        mod = other.module2()
        if mod != 0:
            return ComplexNumber((self.real * other.real + self.im * other.im) / mod,
                                 (self.im * other.real - other.im * self.real) / mod)
        else:
            return ComplexNumber('none (mod = 0)', 'none')
