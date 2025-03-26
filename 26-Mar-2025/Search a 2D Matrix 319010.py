# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        n, m = len(mat), len(mat[0])
        left, right = 0, (m*n)-1

        while left <= right:
            mid = left + (right-left)//2
            val = mat[mid//m][mid%m]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        