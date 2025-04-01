class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binary_toNum(s):
            number = 0
            for i in range(len(s)):
                number += (int(s[i]) * (2**i))
            return number
    
        num1 = binary_toNum(a[::-1])
        num2 = binary_toNum(b[::-1])
        return bin(num1+num2)[2:]