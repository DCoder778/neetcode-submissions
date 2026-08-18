class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        lst = sorted(nums)
        return (lst[-1]*lst[-2]) - (lst[0]*lst[1])

        