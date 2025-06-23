class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m
        def traverse(row, col):
            temp = []
            while inbound(row, col):
                temp.append(mat[row][col])
                row += 1
                col -= 1
            if self.reverse:
                result.extend(temp[::-1])
            else:
                result.extend(temp)
            self.reverse = not self.reverse
        
        result, self.reverse = [], True

        for j in range(m): # horizontal
            traverse(0, j)
            
        for i in range(1, n): # vertical
            traverse(i, m-1)

        return result