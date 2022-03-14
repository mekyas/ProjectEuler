class Solution(object):
    def findDuplicates(self, nums):
        count = [0 for i in nums]
        result = set()
        for n in nums:
            count[n-1] += 1
            if count[n-1]>1:
                result.add(n)
        return result

print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))