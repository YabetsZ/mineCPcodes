class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # simple bfs
        n = len(board)
        # def dest(r, c, right, roll):
        #     dr = r - (c+roll)//n
        #     nRight = right if dr%2==0 else not right
        #     nr, nc = r-dr, -1
        #     if nRight:
        for i in range(n//2):
            board[i], board[n-1-i] = board[n-1-i], board[i]
        for j in range(1, n, 2):
            for i in range(n//2):
                board[j][i], board[j][n-1-i] = board[j][n-1-i], board[j][i]
    
        queue = deque([(0, 0)]) # r, c
        visited = set([0])
        rolls = 0
        while queue:
            rolls += 1
            # print(queue)
            for _ in range(len(queue)):
                r, c = queue.popleft()
                cellNo = r*n+c # 0 indexed
                for i in range(1, 7):
                    newCell = cellNo + i
                    if newCell not in visited and newCell < n**2:
                        visited.add(newCell)
                        nr, nc = newCell//n, newCell%n
                        if board[nr][nc] != -1:
                            visited.add(board[nr][nc]-1)
                            nr, nc = (board[nr][nc]-1)//n, (board[nr][nc]-1)%n
                        if nr*n + nc == n**2-1:
                            return rolls
                        queue.append((nr, nc))
        return -1
        