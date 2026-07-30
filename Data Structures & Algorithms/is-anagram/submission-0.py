class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lis1 = list(s)
        lis2= list(t)
        lis1.sort()
        lis2.sort()
        return lis1 == lis2
