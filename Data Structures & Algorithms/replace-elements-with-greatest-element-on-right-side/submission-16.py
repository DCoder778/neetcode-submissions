class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = float("-inf")
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                maximum = max(arr[j], maximum)
            arr[i] = maximum
            maximum = float("-inf")
        arr[-1] = -1
        return arr
        