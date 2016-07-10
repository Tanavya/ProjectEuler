

#Print all prime numbers below 2 frikking million



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


def isPrime2(number):
    if number == 2:
        return True

    elif number > 1 and number % 2 != 0:
        for current in range(3, int(math.sqrt(number)) + 1, 2):
            if number % current == 0:
                return False
        return True
    return False



"""
Firstly, I suggest you use a better function to check whether a number is prime or not.
Here's a better modification, from https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/ which is an excellent
explanation on generators in Python.

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

Secondly, you need to understand what a Generator actually does. Again Jeff Knupp explains it perfectly.
In short a generator is a function that does not "return" it simply "yields" and takes back control when the next() method is called on it.
So no variables that are created during the function are lost, and memory is saved by not creating the variables defined in the function again and again.

Then you can go on solving Euler 10, which is also explained in the link. :)

Good luck with the rest of the Eulers!
"""


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def solve_number_10():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

def main():
    #solve_number_10()


    for i in range(1,100):
        print i, is_prime(i), isPrime2(i)


if __name__ == "__main__":
    #print is_prime(12)
    main()


