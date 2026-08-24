class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        length = high - low + 1
        count = length //2
        if length % 2 and low % 2:
            count += 1
        return count
        