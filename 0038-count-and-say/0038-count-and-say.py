class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for i in range(n-1):
            new_s = ""
            freq = 1
            for i in range(1,len(s)):
                if s[i] == s[i-1]:
                    freq += 1
                else:
                    new_s += str(freq) + s[i-1]
                    freq = 1
            new_s += str(freq) + s[-1]
            s = new_s
        return s

