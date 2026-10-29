class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = nums.count(val)
        for i in range(0,cnt):
            nums.remove(val)
            nums.append(val)
        return len(nums) - cnt
        