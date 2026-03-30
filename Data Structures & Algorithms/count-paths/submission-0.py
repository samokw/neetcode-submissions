class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # We know that the bottom row will all be zer0 

        for i in range(m - 1): # We calculated the bottom row so we now start calculating the next ones
            newRow = [1] * n
            for j in range(n - 2, -1 , -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
