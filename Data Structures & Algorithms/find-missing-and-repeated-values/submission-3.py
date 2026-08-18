class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        lst = [num for sublist in grid for num in sublist]
        lst.sort()
        num1 = 0
        num2 = 0
        n = len(lst)
        sum =  int((n*(n+1))/2)
        for i in range(0,len(lst)-1):
            if(lst[i] == lst[i+1]):
                num1 = lst[i]
            else:
                sum = sum - lst[i]
        sum = sum - lst[i+1]
        return [num1, sum]