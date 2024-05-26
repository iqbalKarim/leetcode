def countGood(nums, k):
    """
    find good subarrays
    k pairs (i, j):
        i < j
        arr[i] == arr[j]
    sliding window
    """
    subCount = 0
    for start in range(len(nums) - 1):
        for end in range(len(nums), start, -1):
            kCheck = 0
            for middleOuter in range(start, end):
                for middleInner in range(middleOuter + 1, end):
                    if nums[middleOuter] == nums[middleInner]:
                        kCheck += 1
            if kCheck >= k:
                print(nums[start:end], ' : ', kCheck)
                subCount += 1
    return subCount


countGood([3,1,4,3,2,2,4], 2)
