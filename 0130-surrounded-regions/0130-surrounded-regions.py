class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def in_bound(row, col):
            return 0 <= row <= len(board)-1 and 0 <= col <= len(board[0])-1
        def check(row, col):
            checked.add((row, col))
            result = True
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not in_bound(row+dy, col+dx):
                    result = False
                elif (row+dy, col+dx) not in checked and board[row+dy][col+dx] == "O":
                    result = result and check(row+dy, col+dx)
            return result
                
        def change(row, col):
            changed.add((row, col))
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if in_bound(row+dy, col+dx) and (row+dy, col+dx) not in changed and board[row+dy][col+dx] == "O":
                    change(row+dy, col+dx)
            board[row][col] = "X"
        
        checked = set()
        changed = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in checked and check(i, j):
                    change(i, j)
        

