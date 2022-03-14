from typing import List
class Solution:
    result = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, path):
            if not nums:
                self.result.append(path)
                return
            for x in range(len(nums)):
                helper(nums[:x]+nums[x+1:], path+[nums[x]])
        helper(nums, [])
        return self.result

sol = Solution()
print(sol.permute([1, 2, 3]))