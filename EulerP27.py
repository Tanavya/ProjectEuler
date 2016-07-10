#CANT BELIEVE I WROTE THIS ONE, IT LOOKS SO NEAT! <3
import math

def isPrime(n):

    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False

    for current in range(3, int(math.sqrt(n)) + 1, 2):
        if n % current == 0:
            return False
    return True


class Function(object):
    def __init__(self):
        self.a = 1
        self.b = 1

    def copy(self):
        f = Function()
        f.setFunction(self.a, self.b)
        return f

    def setFunction(self, a, b):
        self.a = a
        self.b = b

    def getValue(self, n):
        return n**2 + self.a * n + self.b

    def getFunction(self):
        return self.__str__()

    def __str__(self):
        return "n2 + " + str(self.a) + "n" + " + " + str(self.b)

    def getCoefficients(self):
        return self.a, self.b


f = Function()
MAX = 0,0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        f.setFunction(a,b)
        n = 0
        while isPrime(f.getValue(n)):
            n += 1
        if n > MAX[0]:
            MAX = n, f.copy()

print MAX[0], MAX[1].getFunction(), MAX[1].getCoefficients()[0] * MAX[1].getCoefficients()[1]