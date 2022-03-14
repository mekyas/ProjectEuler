def subsets(nums):
        output = [[]]
        
        for num in nums:
            a = [curr + [num] for curr in output]
            output += a
        return output
print(subsets([1, 2, 3]))