class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        total = 0
        for i in nums:
            if i == 1:
                total = total + 1
                if total > max:
                    max = total
            else:
                total = 0
        return max