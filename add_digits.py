from functools import reduce
def addDigits(num: int) -> int:
    if num<10:
        return num
    else:
        return addDigits(reduce((lambda x, y: x+y), map((lambda x: int(x)), str(num))))

print(addDigits(38))