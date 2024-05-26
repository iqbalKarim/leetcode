class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def generateSubsets(nums, initial_subsets=[], index=0):
            subsets = initial_subsets
            if index == len(nums):
                return subsets
            elif index == 0:
                subsets.append([])
                subsets.append([nums[index]])
                index += 1
                generateSubsets(nums, subsets, index)
            else:
                for i in range(len(subsets) - 1, 0, -1):
                    temp = subsets[i].copy()
                    temp.append(nums[index])
                    subsets.append(temp)
                subsets.append([nums[index]])
                index += 1
                generateSubsets(nums, subsets, index)
            return subsets

        def calcXORSum(subsets):
            total = 0
            for subset in subsets:
                tempTotal = 0
                for num in subset:
                    tempTotal ^= num
                total += tempTotal
            return total

        subsets = generateSubsets(nums)
        return calcXORSum(subsets)

t = Solution()

print(t.subsetXORSum([1, 3]))
