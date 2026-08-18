class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        rep = False
        for num, c in count.items():
            if c > 1:
                rep = True
        return rep
        