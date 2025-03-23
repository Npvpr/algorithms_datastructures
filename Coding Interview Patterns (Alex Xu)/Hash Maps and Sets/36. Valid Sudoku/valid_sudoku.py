class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        big_grid_dict = {}
        row_dict = {}
        col_dict = {}

        for small_row in range(len(board)):
            for small_col in range(len(board[small_row])):

                cur_num = board[small_row][small_col]

                if cur_num.isnumeric():

                    big_row = small_row // 3
                    big_col = small_col // 3
                    
                    # grid check
                    big_name = str(big_row) + str(big_col)
                    if big_name not in big_grid_dict:
                        big_grid_dict[big_name] = set()
                    if cur_num in big_grid_dict[big_name]:
                        return False
                    else:
                        big_grid_dict[big_name].add(cur_num)

                    # row check
                    if small_row not in row_dict:
                        row_dict[small_row] = set()
                    if cur_num in row_dict[small_row]:
                        return False
                    else:
                        row_dict[small_row].add(cur_num)

                    # col check
                    if small_col not in col_dict:
                        col_dict[small_col] = set()
                    if cur_num in col_dict[small_col]:
                        return False
                    else:
                        col_dict[small_col].add(cur_num)

        return True