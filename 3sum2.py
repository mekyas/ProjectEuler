def three_sum(nums):
    nums = sorted(nums)
    n = len(nums)
    result = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        start = i+1
        end = n-1
        target = -1*nums[i]
        while start < end:
            #if nums[start] == nums[start+1]:
            #    start += 1
            #if nums[end] == nums[end -1]:
            #    end -= 1
            if nums[start] + nums[end] == target:
                result.append([nums[i], nums[start], nums[end]])
                start += 1
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
    return result

print(three_sum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))