class Solution:
    # For a question like this its important to ask if you can modify the orginal input otherwise you'd need to use a hashset 
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (min(r, c) < 0) or ROWS == r or c == COLS or grid[r][c] == "0":
                return
            grid[r][c] = "0"

            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands