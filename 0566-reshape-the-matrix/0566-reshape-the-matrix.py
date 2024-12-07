class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        new_mat = []
        matrix = []
        for row in mat:
            for item in row:
                new_mat.append(item)
        if len(new_mat) != r * c:
            return mat
        else:
            for i in range(0,len(new_mat),c):
                matrix.append(new_mat[i: i+c])
        return matrix