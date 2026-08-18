class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        sum = 0
        for i in range(0, len(nums)):
            if(nums[i] == 1):
                sum = sum + 1
                if(sum > max):
                    max = sum
            else:
                sum = 0
        return max

        