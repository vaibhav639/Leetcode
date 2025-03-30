class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s2 = s + s 
        s2 = s2[1:-1]
        if s in s2:
            return True
        return False

        