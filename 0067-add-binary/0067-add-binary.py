class Solution(object):
    def addBinary(self, a, b):
        alen  = len(a)
        blen = len(b)
        carry = 0
        ans = ""
        i = 0
        
        while i < alen or i < blen or carry!=0:
            x = 0
            if i < alen and a[alen-i-1] == "1":
                x = 1
                
            y = 0
            if i < blen and b[blen-i-1] == "1":
                y = 1
                
            ans = str((x + y + carry)%2) + ans
            carry = (x + y + carry)//2
            i+=1
            
        return ans
                
        
        