class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        s = s.lstrip()
        lst = s.split(" ")
        return len(lst[-1])
        