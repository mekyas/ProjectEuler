def four_sum(nums, target):
    n = len(nums)
    nums = sorted(nums)
    result =[]
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
                continue
        for j in range(i+1, n-2):
            if nums[j] == nums[j-1] and nums[i] != nums[j]:
                continue
            tar = target - nums[i]- nums[j]
            start = j+1
            end = n-1
            while start < end:
                if nums[start] == nums[start-1]:
                    start += 1
                if end < n-1 and nums[end] == nums[end+1]:
                    end -= 1
                if nums[start] + nums[end] == tar:
                    result.append([nums[i], nums[j], nums[start], nums[end]])
                    start += 1
                elif nums[start] + nums[end] < tar:
                    start += 1
                else:
                    end -= 1
    return result

print(four_sum([-1,2,2,-5,0,-1,4],3))
                