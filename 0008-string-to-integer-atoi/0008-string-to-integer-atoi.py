class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  
        if not s:
            return 0
        
        flagNegative = False
        output = ""

        if s[0] == "-":
            flagNegative = True
            s = s[1:]  
        elif s[0] == "+":
            s = s[1:]  

        
        for char in s:
            if char.isdigit():
                output += char
            else:
                break  

        if output:
            num = int(output)
            if flagNegative:
                num = -num

                
            INT_MAX = 2**31 - 1
            INT_MIN = -2**31
            if num > INT_MAX:
                return INT_MAX
            if num < INT_MIN:
                return INT_MIN

            return num
        else:
            return 0