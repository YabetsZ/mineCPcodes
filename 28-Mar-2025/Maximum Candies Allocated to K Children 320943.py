# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(num, k):
            if num == 0:
                return True
            count = 0
            for candy in candies:
                count += candy//num
            return count >= k
        left, right = 0, max(candies)
        best = 0
        while left <= right:
            mid = left + (right - left)//2

            if check(mid, k):
                best = mid
                left = mid + 1
            else:
                right = mid-1
        return best
