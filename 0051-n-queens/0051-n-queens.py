class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        main_diagonal = set()
        secondary_diagonal = set()
        result = []
        def place(row, unique):
            if row == n:
                return
            for col in range(n):
                if (col not in columns and
                    row - col not in main_diagonal and
                    row + col not in secondary_diagonal):

                    columns.add(col)
                    main_diagonal.add(row-col)
                    secondary_diagonal.add(row+col)

                    rowString = "".join(["."*col, "Q", "."*(n-col-1)])
                    unique.append(rowString)

                    if row == n-1:
                        result.append(unique[:])
                    place(row+1, unique)
                    unique.pop()

                    columns.discard(col)
                    main_diagonal.discard(row-col)
                    secondary_diagonal.discard(row+col)
        place(0, [])
        return result