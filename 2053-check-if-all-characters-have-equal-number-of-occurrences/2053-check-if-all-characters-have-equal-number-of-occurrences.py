class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}

        for char in s:
            dic[char] = dic.get(char,0) + 1

        values = dic.values()
        if len(set(values)) == 1:
            return True
        return False
        