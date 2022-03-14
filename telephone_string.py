"""
Given a string containing digits from 0-9, using the corresponding alphabet
on the  telephone pad, return all possible letter combinations that the number
could represent. Note, that 0 and 1 do not map to any letters.
For example, if you're given [2, 3, 4], your function should return 27 3-letter combinations:

['a', 'd', 'g'] ['a', 'd', 'h']['a', 'd', 'i']
['a', 'e', 'g']['a', 'e', 'h']['a', 'e', 'i']
['a', 'f', 'g']['a', 'f', 'h']['a', 'f', 'i']
['b', 'd', 'g']['b', 'd', 'h']['b', 'd', 'i']
['b', 'e', 'g']['b', 'e', 'h']['b', 'e', 'i']
['b', 'f', 'g']['b', 'f', 'h']['b', 'f', 'i']
['c', 'd', 'g']['c', 'd', 'h']['c', 'd', 'i']
['c', 'e', 'g']['c', 'e', 'h']['c', 'e', 'i']
['c', 'f', 'g']['c', 'f', 'h']['c', 'f', 'i']
"""

telephone_pad = {
    2:['a', 'b', 'c'],
    3:['d', 'e', 'f'],
    4:['g', 'h', 'i'],
    5:['j', 'k', 'l'],
    6:['m', 'n', 'o'],
    7:['p', 'q', 'r', 's'],
    8:['t', 'u', 'v'],
    9:['w', 'x', 'y', 'z']
}

def helper(numbers, index, current, output):
    if len(current) == len(numbers):
        print(current)
        output.append(current)
        return
    for letter in telephone_pad[numbers[index]]:
        current.append(letter)
        helper(numbers, index+1, current, output)
        current.pop(-1)

def evaluate_text(numbers):
    output = []
    helper(numbers, 0, [], output)
    return output

if __name__ == "__main__":
    print(evaluate_text([2, 3, 4]))

