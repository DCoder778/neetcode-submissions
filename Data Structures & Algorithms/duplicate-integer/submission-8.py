class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        repeat = False
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                repeat = True
        return repeat