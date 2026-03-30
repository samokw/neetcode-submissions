class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()

        def exploreRoom(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == -1):
                return
            queue.append((r, c))
            visit.add((r, c))

        # Finding all the gates in the matrix
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visit.add((r, c))
        gate_distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = gate_distance
                exploreRoom(r + 1, c)
                exploreRoom(r - 1, c)
                exploreRoom(r, c + 1)
                exploreRoom(r, c - 1)
            gate_distance += 1 