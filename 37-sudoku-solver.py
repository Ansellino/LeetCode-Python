
''' answer with 998 ms '''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.rows = [[False] * 9 for _ in range(9)]
        self.cols = [[False] * 9 for _ in range(9)]
        self.boxes = [[False] * 9 for _ in range(9)]
        self.board = board
        self.possibilities = [[set('123456789') for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    self.rows[i][num] = True
                    self.cols[j][num] = True
                    self.boxes[(i // 3) * 3 + (j // 3)][num] = True
                    self.possibilities[i][j] = set()  # Remove possibilities for filled cells

        self.backtrack(0, 0)

    def backtrack(self, row, col) -> bool:
        if col == 9:
            row += 1
            col = 0
        if row == 9:
            return True

        if self.board[row][col] != '.':
            return self.backtrack(row, col + 1)

        for num in self.possibilities[row][col]:
            num = int(num) - 1
            if self.is_valid(row, col, num):
                self.board[row][col] = str(num + 1)
                self.rows[row][num] = True
                self.cols[col][num] = True
                self.boxes[(row // 3) * 3 + (col // 3)][num] = True

                if self.backtrack(row, col + 1):
                    return True

                self.board[row][col] = '.'
                self.rows[row][num] = False
                self.cols[col][num] = False
                self.boxes[(row // 3) * 3 + (col // 3)][num] = False

        return False

    def is_valid(self, row, col, num):
        return not (
            self.rows[row][num] or 
            self.cols[col][num] or 
            self.boxes[(row // 3) * 3 + (col // 3)][num]
        )

''' answer with 2153 ms 
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.rows = [[False] * 9 for _ in range(9)]
        self.cols = [[False] * 9 for _ in range(9)]
        self.boxes = [[False] * 9 for _ in range(9)] 
        self.board = board

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    self.rows[i][int(board[i][j]) - 1] = True
                    self.cols[j][int(board[i][j]) - 1] = True
                    self.boxes[(i // 3) * 3 + (j // 3)][int(board[i][j]) - 1] = True

        self.backtrack(0, 0)

    def backtrack(self, row, col) -> bool:
        if col == 9:
            row += 1
            col = 0
        if row == 9:
            return True

        if self.board[row][col] != '.':
            return self.backtrack(row, col + 1)

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = str(num)
                self.rows[row][num - 1] = True
                self.cols[col][num - 1] = True
                self.boxes[(row // 3) * 3 + (col // 3)][num - 1] = True
                if self.backtrack(row, col + 1):
                    return True
                self.board[row][col] = '.'
                self.rows[row][num - 1] = False
                self.cols[col][num - 1] = False
                self.boxes[(row // 3) * 3 + (col // 3)][num - 1] = False

        return False

    def is_valid(self, row, col, num):
        return not (
            self.rows[row][num - 1] or 
            self.cols[col][num - 1] or 
            self.boxes[(row // 3) * 3 + (col // 3)][num - 1]
        )
'''
