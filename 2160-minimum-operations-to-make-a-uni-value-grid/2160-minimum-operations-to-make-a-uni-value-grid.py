class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        lst = [num for sub in grid for num in sub]
        rem = lst[0] % x
        for num in lst:
            if num % x != rem:
                return -1
        lst.sort()
        median = lst[len(lst)//2]
        count = 0
        for num in lst:
            count+= (abs(num-median)//x)
        return count