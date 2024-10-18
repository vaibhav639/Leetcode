class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) -1

        while l < r:
            top = l
            bottom = r

            for i in range(r - l):
                # store the top left
                top_left = matrix[top][l + i]

                # change bottom left to top left
                matrix[top][l + i] = matrix[bottom-i][l]

                # change bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r - i]

                # change top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # change top right to top left
                matrix[top + i][r] = top_left

            r -= 1
            l += 1