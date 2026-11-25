class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            maximum = arr[i+1]
            for j in range(i+1,len(arr)):
                maximum = max(maximum,arr[j])
            arr[i] = maximum
        arr[-1] = -1
        return arr
