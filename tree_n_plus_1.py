import sys

def cycle(num):
    i = 1
    while (num != 1):
        if num%2 == 1:
            num = 3*num+1
        else:
            num /= 2
        i += 1
    return i
def max_cycle(i, j):
    max_c = 0
    for k in range(i, j+1):
        curr= cycle(k)
        if curr > max_c:
            max_c = curr
    print(i,' ', j,' ' ,max_c)

if __name__ == "__main__":
    input()
    for line in sys.stdin:
        i, j = (int(k) for k in line.split())
        max_cycle(i, j)