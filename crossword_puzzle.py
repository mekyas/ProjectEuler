import math
import os
import random
import re
import sys



def crosswordPuzzle(crossword, words):
    if len(words)==0:
        return crossword
    next_word = words.pop(0)
    found = False
    # iterate by row
    for row in range(10):
        for col in range(10-len(next_word)):
            if not found and crossword[row][col]=='-':
                start = 0
                while start<len(next_word) and crossword[row][col+start] in ['-', next_word[start]]:
                    start +=1
                if start==len(next_word):
                    start = 0
                    found = True
                    while start<len(next_word):
                        crossword[row][col+start] = next_word[start]
                        start +=1
    for col in range(10):
        for row in range(10-len(next_word)):
            if not found and crossword[row][col]=='-':
                start = 0
                while start<len(next_word) and crossword[row+start][start] in ['-', next_word[start]]:
                    start +=1
                if start==len(next_word):
                    start = 0
                    found = True
                    while start<len(next_word):
                        crossword[row][col+start] = next_word[start]
                        start +=1
    if found:
        crosswordPuzzle(crossword, words)
    else:
        words.append(next_word)
        return


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []
    inputs = ["+-++++++++",
                "+-++++++++",
                "+-++++++++",
                "+-----++++",
                "+-+++-++++",
                "+-+++-++++",
                "+++++-++++",
                "++------++",
                "+++++-++++",
                "+++++-++++"]
    for i in range(10):
        crossword_item = inputs[i]
        crossword.append(list(crossword_item))

    # words = input()
    words = ["LONDON", "DELHI", "ICELAND", "ANKARA"]

    result = crosswordPuzzle(crossword, words)

    print(result)
    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()