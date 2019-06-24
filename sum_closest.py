def sum_closest(nums, target):
    nums = sorted(nums)
    n = len(nums)
    min_result = 2**31
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        start = i+1
        end = n-1
        while start < end:
            #if nums[start] == nums[start+1]:
            #    start += 1
            #if nums[end] == nums[end -1]:
            #    end -= 1
            temp = nums[start] + nums[end] + nums[i]
            if temp == target:
                return target
            elif temp < target:
                start += 1
            else:
                end -= 1
            if abs(target- temp) < abs(target-min_result):
                    min_result = temp
    return min_result

print(sum_closest([-1,0,1,1,55], 3))