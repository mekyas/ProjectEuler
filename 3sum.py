from collections import defaultdict

def is_duplicate(ar1, ar2):
    if ar2 == []:
        return False
    for i in ar2:
        som = 0
        if set(ar1) == set(i):
            return True
    return False

def three_sum(array):
    two_sum = defaultdict(list)
    result = []
    n = len(array) 
    for i in range(n-1):
        for j in range(i+1, n):
            two_sum[array[i]+array[j]].append([[array[i], array[j]],set([i, j])])
    look_up = [-k for k in two_sum.keys()]
    for val in look_up:
        if val in array:
            i = array.index(val)
            for j in two_sum[-val]:
                temp = [val]+ j[0]
                if not is_duplicate(temp, result):
                    s = j[1]
                    s.add(i)
                    if len(s)== 3:
                        result.append(temp)
    return result


#print(is_duplicate([0, 1, -1], [[-3, 0, 3],[0, 0, 0]]))
print(three_sum([-2,-7,-11,-8,9,-7,-8,-15,10,4,3,9,8,11,1,12,-6,-14,-2,-1,-7,-13,-11,-15,11,-2,7,-4,12,7,-3,-5,7,-7,3,2,1,10,2,-12,-1,12,12,-8,9,-9,11,10,14,-6,-6,-8,-3,-2,14,-15,3,-2,-4,1,-9,8,11,5,-14,-1,14,-6,-14,2,-2,-8,-9,-13,0,7,-7,-4,2,-8,-2,11,-9,2,-13,-10,2,5,4,13,13,2,-1,10,14,-8,-14,14,2,10]))
