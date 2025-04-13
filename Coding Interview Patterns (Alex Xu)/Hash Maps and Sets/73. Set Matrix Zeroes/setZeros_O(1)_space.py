class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zero = False
        first_col_zero = False

        # check zeroes
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    # first row, other columns
                    if row == 0:
                        first_row_zero = True
                    # other rows
                    else:
                        matrix[row][0] = 0

                    # first col, other rows
                    if col == 0:
                        first_col_zero = True
                    # other cols
                    else:
                        matrix[0][col] = 0

        # update zeroes for other rows and cols (excluding first ones)
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # check first row zero
        if first_row_zero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0

        # check first col zero
        if first_col_zero:
            for row in range(len(matrix)):
                matrix[row][0] = 0
