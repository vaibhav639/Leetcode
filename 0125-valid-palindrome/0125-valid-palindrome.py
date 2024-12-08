class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for char in s:
            if char.isalnum():
                s1 += char.lower()

        s2 = s1[::-1]

        if s1 == s2:
            return True
        else:
            return False
        