class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0


        def rot(r, c):
            if (r in range(ROWS) and c in range(COLS) and grid[r][c] == 1):
                grid[r][c] = 2
                queue.append((r, c))
                return -1
            return 0
        # We need to where the rotten fruit are and how many fresh fruit there are
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: 
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                fresh += rot(r + 1, c)
                fresh += rot(r - 1, c)
                fresh += rot(r, c + 1)
                fresh += rot(r, c - 1)
            time += 1
        return time if fresh == 0 else -1