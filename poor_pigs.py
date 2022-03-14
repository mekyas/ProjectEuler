class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        from math import ceil
        rounds = ceil(minutesToTest/minutesToDie)
        prod = 1
        x = rounds
        tested=1
        while tested<buckets:
            prod=1
            for j in range(1, rounds):
                prod *= (x+2-j)
            tested = 2**(x - rounds+1)*prod
            x+=1
        return x-1

solu = Solution()
print(solu.poorPigs(4, 15, 15))