import math
def is_prime(number):
    while True:
        if number == 2:
            return True
        elif number > 1 and number % 2 != 0:
            for current in range(3, int(math.sqrt(number) + 1), 2):
                if number % current == 0:
                    return False
            return True
        return False

def isCircularPrime(n):


    for i in range(len(str(n))):

        n = str(n)[1:] + str(n)[0]
        if not is_prime(int(n)):
            return False

    return True


print isCircularPrime(537)



count = 0
for i in range(1,100):
    if isCircularPrime(i):
        count += 1

print count

