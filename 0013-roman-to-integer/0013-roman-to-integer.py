class Solution:
    def romanToInt(self, s: str) -> int:
        summ = 0
        last = 0
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        last = 0
        for i in range(len(s)-1,-1,-1):
            curr = dic[s[i]]

            if curr < last:
                summ -= curr
            else:
                summ += curr
            last = curr

        return summ

        