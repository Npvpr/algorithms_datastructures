class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        queue = deque([])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append([row, col])
        
        while queue:
            print(queue)
            rot_change = False
            for i in range(len(queue)):
                cur_list = queue.popleft()
                cur_row = cur_list[0]
                cur_col = cur_list[1]

                if grid[cur_row][cur_col] == -1 or grid[cur_row][cur_col] == 0:
                    continue
                
                if grid[cur_row][cur_col] == 1:
                    rot_change = True
                grid[cur_row][cur_col] = -1 # for both 2 and 1

                # up
                if cur_row - 1 >= 0:
                    queue.append([cur_row-1, cur_col])
                
                # down
                if cur_row + 1 < len(grid):
                    queue.append([cur_row+1, cur_col])

                # left
                if cur_col - 1 >= 0:
                    queue.append([cur_row, cur_col-1])

                # right
                if cur_col + 1 < len(grid[0]):
                    queue.append([cur_row, cur_col+1])

            if rot_change == True:
                mins += 1

        print(grid)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        return mins