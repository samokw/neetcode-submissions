class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = [set() for _ in range(9)]
        seen_cols = [set() for _ in range(9)]
        seen_box = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                if val in seen_rows[r]:
                    return False
                if val in seen_cols[c]:
                    return False
                br, bc = r // 3, c // 3
                if val in seen_box[br][bc]:
                    return False
                seen_rows[r].add(val)
                seen_cols[c].add(val)
                seen_box[br][bc].add(val)
        return True