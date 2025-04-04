class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int: # type: ignore

        count_map = {}
        max_count = 0

        def count(row, col):
            cur_node = matrix[row][col]
            key = str(row) + "-" + str(col)
            
            if key in count_map:
                return count_map[key]
            count_list = [1] * 4

            # up
            if row - 1 >= 0 and cur_node > matrix[row-1][col]:
                count_list[0] = count_list[0] + count(row-1, col)

            # down    
            if row + 1 < len(matrix) and cur_node > matrix[row+1][col]:
                count_list[1] = count_list[1] + count(row+1, col)

            # left
            if col - 1 >= 0 and cur_node > matrix[row][col-1]:
                count_list[2] = count_list[2] + count(row, col-1)

            #  right
            if col + 1 < len(matrix[0]) and cur_node > matrix[row][col+1]:
                count_list[3] = count_list[3] + count(row, col+1)

            count_list.sort()
            count_map[key] = count_list[-1]
            return count_list[-1]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                max_count = max(max_count, count(row, col))

        return max_count
        