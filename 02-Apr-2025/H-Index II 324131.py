# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def condition(mid):
            n = len(citations)
            if mid <= n and citations[n-mid] >= mid:
                return True
            False
        left, right = 1, 1000
        best = 0
        while left <= right:
            mid = (right+left)//2
            if condition(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        return best

