import random
import bisect
from collections import Counter
import math

class Solution:
    def __init__(self, s, m, c):
        self.c = c
        self.s = s
        self.m = m
        # the probability of the point at c
        v = 2/(m-s+2)

        # cumulative function at c P(X<=c)
        self.F_c = ((c-s+1)*v)/2

        # calculate the F-1 inverse of the CDF function
        self.Y_u_1 = lambda u: math.sqrt(2*((c-s+1)*u)/v) + s -1

        self.Y_u_2 = lambda u: m+ 1 - math.sqrt((2*(m+1-c)*(1-u))/v)


    def generate(self):
        u = random.random()
        if u<=self.F_c:
            val = self.Y_u_1(u)
        else:
            val = self.Y_u_2(u)
        if math.ceil(val)-val < val - int(val):
            ans = math.ceil(val)
        else:
            ans = int(val)
        if ans==(self.m+1) or ans==(self.s-1):
            ans= self.c
        return ans



if __name__=="__main__":
    solution = Solution(2, 7, 6)
    values = []
    for i in range(100000):
        val = solution.generate()
        values.append(val)
    count = Counter(values)
    summ = sum(count.values())
    probabilities = {k:v/summ for k,v in count.items()}
    print("values probabilities\n", probabilities)
    # plot a histogram, set max value to 50
    max_val = max(probabilities.values())
    for k in sorted(count):
        print("{}:{}".format(k, "+"*int((probabilities[k]*50)/max_val)))