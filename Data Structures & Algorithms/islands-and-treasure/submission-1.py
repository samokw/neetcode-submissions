class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        dist = 0
        def explore(r, c):
            if (min(r, c) < 0 
			or r == ROWS 
			or c == COLS 
			or (r, c) in visit
			or grid[r][c] == -1):
                return
            visit.add((r, c))
            queue.append((r, c))

        # Find all the treasure chests
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    queue.append((r, c))
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist 
                explore(r, c + 1)
                explore(r, c - 1)
                explore(r + 1, c)
                explore(r - 1, c)
            dist += 1