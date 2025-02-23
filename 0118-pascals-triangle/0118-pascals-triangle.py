class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        for _ in range(numRows-1):
            last = result[-1]
            emp = []
            i = 0
            j = len(last)-1
    
            if not emp:
                emp.append(last[i])
            while i < j:
                emp.append(last[i]+last[i+1])
                i+=1
            emp.append(last[j])
            result.append(emp)
    
        return result