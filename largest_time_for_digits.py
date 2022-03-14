from typing import List

def largestTimeFromDigits(A: List[int]) -> str:
        from itertools import permutations 
        l = list(permutations(A))
        constrain = [2, 3, 5, 9]
        max_time = -1
        best = -1
        
        def acceptable(p):
            if p[0] <=1:
                constrain[1] = 9
            elif p[0]==2:
                constrain[1] = 3
            else:
                return False
            for j in range(len(constrain)):
                if p[j]> constrain[j]:
                    return False
            return True
        
        def time(p):
            return p[0]*600 + p[1]*60 + p[2]*10 + p[3]
        
        for i, p in enumerate(l):
            if acceptable(p):
                if time(p)>max_time:
                    max_time = time(p)
                    best = i
        return "{}{}:{}{}".format(*l[best]) if best>-1 else ""

print(largestTimeFromDigits([0,0,1,0]))