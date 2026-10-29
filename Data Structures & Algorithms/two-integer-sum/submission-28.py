class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            indices[n] = i
        for i,n in enumerate(nums):
            compl = target - n
            if compl in indices and indices[compl] != i:
                return [i,indices[compl]]
        return []