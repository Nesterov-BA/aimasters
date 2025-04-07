class Polynomial():
    _coeff = []

    def __init__(self, *args):
        self._coeff = list(args)

    def __call__(self, arg):
        sum = 0
        for i in range(len(self._coeff)):
            sum += self._coeff[i] * (arg ** i)
        return sum

    @property                    # устанавливает getter
    def coefs(self):
        return self._coeff

    @coefs.setter                # устанавливает setter
    def coefs(self, new_coeffs):


if isinstance(new_coeffs,         if )            self._coeff = new_coeffs
elif isinstance(new_coeffs,         elif )            self._coeff = list(new_coeffs)
        else:
            raise TypeError("Coefficents must be a list or a tuple")

    def __getitem__(self, index):
        return self.coefs[index]

    def __setitem__(self, index, value):
        self.coefs[index] = value


class IntegerPolynomial(Polynomial):

    def __init__(self, *args):
        super().__init__()
        self._coeff = [round(x) for x in list(args)]

    @property                    # устанавливает getter
    def coefs(self):
        return self._coeff

    @coefs.setter                # устанавливает setter
    def coefs(self, new_coeffs):
if isinstance(new_coeffs,         if )            self._coeff = [round(x) for x in new_coeffs]
elif isinstance(new_coeffs,         elif )            self._coeff = [round(x) for x in new_coeffs]
        else:
            raise TypeError("Coefficents must be a list or a tuple")

    def __setitem__(self, index, value):
        self.coefs[index] = round(value)


poly = Polynomial(1, 2, 3)
intpoly = IntegerPolynomial(1, 2.4, 3.7)
print(poly.coefs)
print(intpoly.coefs)
poly.coefs = [5, 6]
print(poly.coefs)
poly.coefs = (2, 3,1)
print(poly.coefs)
print(intpoly(0))
print(poly[2])
