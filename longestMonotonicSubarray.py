def monotonicSubarray(nums):
    longest = 1
    current = nums[0]
    len = 1
    direction = True

    for num in nums[1:]:
        if current < num:
            if direction:
                len += 1
            else:
                direction = True
                len = 2
        elif current > num:
            if not direction:
                len += 1
            else:
                direction = False
                len = 2
        else:
            len = 1
        current = num
        if len > longest: longest = len

    print(longest)
monotonicSubarray([1,2,3,4,5,3,3,2,1,2,3,4,5,6])