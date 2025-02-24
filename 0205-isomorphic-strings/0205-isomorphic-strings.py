class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map1 = {}
        map2 = {}

        for i in range(len(s)):
            char1, char2 = s[i], t[i]

            if (char1 in map1 and map1[char1] != char2) or (char2 in map2 and map2[char2] != char1):
                return False

            map1[char1] = char2
            map2[char2] = char1
        return True 