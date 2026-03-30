class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        max_size = 0

        def bfs(r, c):
            size = 1
            queue.append((r, c))
            visit.add((r, c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r, c) in visit:
                        continue
                    queue.append((r,c))
                    visit.add((r, c))
                    size += 1
            return size
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_size = max(max_size, bfs(r, c))
        return max_size