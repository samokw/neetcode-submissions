class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowRow, lowCol, highRow, highCol = 0, 0, len(matrix) - 1, len(matrix[0]) - 1

        while lowRow <= highRow:
            midRow = (lowRow + highRow) // 2
            lowCol, highCol = 0, len(matrix[0]) - 1 
            print(midRow)
            while lowCol <= highCol:
                midCol = (lowCol + highCol) // 2
                print(midRow, midCol)
                if target == matrix[midRow][midCol]:
                    return True
                elif target > matrix[midRow][midCol]:
                    lowCol = midCol + 1
                else:
                    highCol = midCol - 1
            if target > matrix[midRow][midCol]:
                lowRow = midRow + 1
            else:
                highRow = midRow - 1
        return False