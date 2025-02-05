class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for sublist in matrix:
            if target in sublist:
                return True
            else:
                continue

        return False