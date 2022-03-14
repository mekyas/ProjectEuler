from typing import List

def largestOverlap(A: List[List[int]], B: List[List[int]]) -> int:
        size = len(A)
        from collections import deque
        a = deque()
        b = deque()
        for i in range(size):
            a.extend(A[i])
            b.extend(B[i])
        overlap = 0
        for x in range(size):
            a.rotate(1)
            for y in range(size):
                cur = a.copy()
                cur.rotate(size*y)
                cur_overlap = 0
                for i,c,d in zip(range(size*size), cur, b):
                    if (i>=size*y and i%size>=x):
                        cur_overlap += c*d
                overlap = max(overlap, cur_overlap)
        return overlap

print(largestOverlap([[0,0,0],[1,0,0],[1,0,0]],
[[1,0,0],[1,1,1],[0,0,1]]))