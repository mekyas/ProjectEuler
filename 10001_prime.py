from math import sqrt

def is_prime(x):
    if x in [1, 2]:
        return True
    for elt in range(2, int(sqrt(x))+1):
        if x % elt == 0:
            return False
    return True

i = 0
k=0
limit= 10001
while i <= limit:
    k += 1
    if is_prime(k):
        i += 1
print(k)