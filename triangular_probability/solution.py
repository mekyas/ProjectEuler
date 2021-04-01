import random
import bisect
from collections import Counter


class Solution:
    # let the height of c be 1, let's calculate the height of each number
    # we will use equalities between the tangente angles to get the height
    # their is two angles, one before c and one after c
    def __init__(self, s, m, c):
        heights = []
        for i in range(s, m+1):
            if i<=c:
                heights.append((i-(s-1))/(c-(s-1)))
            else:
                heights.append((m+1-i)/(m+1-c))
        summ = sum(heights)
        # calculate probabilities
        # sort probabilites and cumulate the cum
        heights = sorted([[h/summ, i] for i, h in zip(range(s, m+1), heights)])
        self.probabilities, self.values  = map(list, list(zip(*heights)))
        prev = 0
        for i, p in enumerate(self.probabilities):
            self.probabilities[i] = prev + p
            prev = self.probabilities[i]

    def generate(self):
        rand = random.random()
        indx = bisect.bisect_left(self.probabilities, rand)
        return self.values[indx]


if __name__=="__main__":
    solution = Solution(2, 7, 6)
    values = []
    for i in range(100000):
        values.append(solution.generate())
    count = Counter(values)
    summ = sum(count.values())
    probabilities = {k:v/summ for k,v in count.items()}
    print("values probabilities\n", probabilities)
    # plot a histogram, set max value to 50
    max_val = max(probabilities.values())
    for k in sorted(count):
        print("{}:{}".format(k, "+"*int((probabilities[k]*50)/max_val)))