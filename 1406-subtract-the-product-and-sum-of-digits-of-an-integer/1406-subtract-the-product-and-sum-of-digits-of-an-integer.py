class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)

        prod = 1
        summ = 0
        for char in s:
            prod*= int(char)
            summ+= int(char)
        
        return prod - summ
        
    

        