class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows_set = set()
        zero_cols_set = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows_set.add(row)
                    zero_cols_set.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zero_rows_set or col in zero_cols_set:
                    matrix[row][col] = 0
