class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0,len(arr)-1):
            max = arr[i+1]
            index = i+1
            for j in range(i+1, len(arr)):
                if arr[j] > max:
                    max = arr[j]
                    index = j
            arr[i] = max
        arr[-1] = -1
        return arr
        