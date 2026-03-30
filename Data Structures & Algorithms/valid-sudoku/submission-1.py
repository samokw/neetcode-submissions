class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = [set() for _ in range(9)]
        seen_col = [set() for _ in range(9)]
        seen_box = [[set() for _ in range(3)] for _ in range(3)]


        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen_row[r]:
                    return False
                if val in seen_col[c]:
                    return False
                box_col, box_row = c // 3, r // 3
                if val in seen_box[box_row][box_col]:
                    return False
                
                seen_row[r].add(val)
                seen_col[c].add(val)
                seen_box[box_row][box_col].add(val)
        return True

