import collections
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        dic = collections.defaultdict(set)

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    dic["r"].add(r)
                    dic["c"].add(c)

        for r in range(row):
            for c in range(col):
                if r in dic["r"] or c in dic["c"]:
                    matrix[r][c] = 0
            
        