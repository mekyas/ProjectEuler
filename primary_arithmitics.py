from itertools import zip_longest
import sys

def carry(a, b):
    """return the number of carry in a 
    some operationof two numbers"""
    carr = 0 # variable to count the number of carry
    a, b = a[::-1], b[::-1]
    for i, j in zip_longest(a, b):
        prev_carry = 0 # variable to indicate that there is a carry in last cal
        if i is None:
            c = 0
            d = int(j)
        elif j is None:
            c = int(i)
            d = 0
        else:
            c = int(i)
            d = int(j)
        if c + d + prev_carry > 9:
            carr += 1
            prev_carry = 1
    if carr == 0:
        print('No carry operation.')
    elif carr == 1:
        print('1 carry operation.')
    else:
        print(carr, ' carry operations.')

if __name__ == "__main__":
    args = 
    i, j = (k for k in input())
    while i != '0' and j != '0':
        carry(i, j)
        i, j = (k for k in input().split())