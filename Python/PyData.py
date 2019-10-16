# My walkthrough code from PyData Seattle 2017 to learn 
# new implenetations and ways to do things in Python

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs
    def __repr__(self):
        return 'Polynomail(*{!r})'.format(self.coeffs)
    def __add__(self, other):
        return Polynomial(*(x+y for x, y in zip(self.coeffs, other.coeffs)))
    def __len__(self): #size of polynomial based on its degree 
        return len(self.coeffs)


p1 = Polynomial(1, 2, 3) # x^2 + 2x + 3
p2 = Polynomial(3, 4, 3) # 3x^2 + 4x + 3
