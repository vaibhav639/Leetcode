class Solution:
    def isThree(self, n: int) -> bool:
        count = 0

        for i in range(1,n+1):
            if count > 3:
                return False
            if n % i==0:
                count+=1
        if count == 3:
            return True
        return False


        