class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0
        
        negative = x < 0
        x = abs(x)
        
        rem =0 
        num =0
        
        while x > 0:
            rem = x%10
            num = num * 10 + rem
            x = x // 10
            
        if negative:
            num = -num
            
        if num < -2**31 or num > 2**31-1:
            return 0
        
        return num
        
        
            
        