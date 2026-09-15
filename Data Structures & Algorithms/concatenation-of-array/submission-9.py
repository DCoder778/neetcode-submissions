class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lst = []
        for j in range(2):
            for i in range(len(nums)):
                lst.append(nums[i])
        return lst