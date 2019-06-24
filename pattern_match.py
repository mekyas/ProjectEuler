from collections import deque

def search(f, pattern, history):
    prev_lines = deque(maxlen=history)
    for line in f:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)

if __name__ == '__main__':
    with open('pattern_match.txt') as f:
        for line, prevlines in search(f, 'in', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)