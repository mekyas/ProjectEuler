phone_comb = {
    '2':{'a', 'b', 'c'},
    '3':{'d', 'e', 'f'},
    '4':{'g', 'h', 'i'},
    '5':{'j', 'k', 'l'},
    '6':{'m', 'n', 'o'},
    '7':{'p', 'q', 'r', 's'},
    '8':{'t', 'u', 'v'},
    '9':{'w', 'x', 'y', 'z'}
}
from itertools import product
def letter_combination(string):
    elt = [phone_comb[i] for i in string]
    prod = list(product(*elt))
    prod = [''.join(i) for i in prod]
    return prod
print(letter_combination("23"))