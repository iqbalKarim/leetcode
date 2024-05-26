def countGood(nums, k):
    """
    find good subarrays
    k pairs (i, j):
        i < j
        arr[i] == arr[j]
    """
    def makeSubarrays(nums):
        subs = []
        for start in range (len(nums) - 2):
            for end in range (len(nums), start + 2, -1):
                subs.append(nums[start:end])
        return (subs)

    def checkGood(sub, k):
        nPairs = 0
        for control, i in enumerate(sub):
            for j in (sub[control + 1:]):
                if i == j:
                    nPairs += 1
        if nPairs < k:
            return False
        return True

    goods = 0
    for sub in makeSubarrays(nums):
        if checkGood(sub, k):
            goods += 1

    print (goods)


countGood([3,1,4,3,2,2,4], 2)