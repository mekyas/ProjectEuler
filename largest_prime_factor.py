from math import sqrt


def is_prime(x):
    if x in [1, 2]:
        return True
    for elt in range(2, int(sqrt(x))+1):
        if x % elt == 0:
            return False
    return True


def prime_factor(y):
    max_fact = 0
    for dev in range(1,int(sqrt(y))):
        if y%dev == 0 and is_prime(dev):
            if dev > max_fact:
                max_fact = dev
        dev += 1
    return max_fact

print(prime_factor(600851475143))
