class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        hor, ver, blk = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    hor[i].add(board[i][j])
                    ver[j].add(board[i][j])
                    blk[i//3*3 + j//3].add(board[i][j])
        def backtrack(node):
            if node == 81:
                return True
            i, j = node//9, node%9
            if board[i][j] != ".":
                return backtrack(node+1)

            for c in range(1, 10):
                c = str(c)
                if c not in hor[i] and c not in ver[j] and c not in blk[i//3*3 + j//3]:
                    board[i][j] = c
                    hor[i].add(c)
                    ver[j].add(c)
                    blk[i//3*3 + j//3].add(c)
                    if not backtrack(node+1):
                        board[i][j] = "."
                        hor[i].discard(c)
                        ver[j].discard(c)
                        blk[i//3*3 + j//3].discard(c)
                    else:
                        return True

            return False
        
        backtrack(0)