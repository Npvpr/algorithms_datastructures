class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: # type: ignore
        
        if not grid:
            return 0

        visited = set()
        row_len = len(grid)
        col_len = len(grid[0])
        count = 0
        for row in range(row_len):
            for col in range(col_len):
                cur_str = str(row) + " " + str(col)
                if cur_str not in visited:
                    if grid[row][col] == "1":
                        self.check(row, col, visited, grid)
                        count += 1

        return count

    def check(self, row, col, visited, grid):
        cur_str = str(row) + "+" + str(col)
        if cur_str in visited:
            return

        visited.add(str(row) + str(col))

        if grid[row][col] != "1":
            return
        else:
            # up
            if row - 1 >= 0:
                self.check(row-1, col, visited, grid)

            # down    
            if row + 1 < len(grid):
                self.check(row+1, col, visited, grid)

            # left
            if col - 1 >= 0:
                self.check(row, col-1, visited, grid)

            #  right
            if col + 1 < len(grid[0]):
                self.check(row, col+1, visited, grid)
            

        