# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

def maximizeSum(nums, k: int) -> int:
    max = nums[0]
    index = 0
    total = 0
    for i in range(1, len(nums)):
        if max < nums[i]:
            index = i
            max = nums[i]
    total += nums[index]
    if (k > 1):
        del nums[index]
        nums.append(max + 1)
    for reps in range(k - 1):
        total += nums[-1]
        nums.append(nums[-1] + 1)
        del nums[-2]
    return total

nums = [5,5,5]
print(maximizeSum(nums, 3))