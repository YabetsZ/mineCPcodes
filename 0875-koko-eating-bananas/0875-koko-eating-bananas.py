class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(limit):
            count = 0
            for pile in piles:
                count += math.ceil(pile/limit)
            return count
        left, right = 1, max(piles)
        best = -1
        while left <= right:
            mid = left + (right - left)//2
            new_h = helper(mid)
            if new_h > h:
                left = mid + 1
            elif new_h < h:
                right = mid - 1
            else:
                best = mid
                right = mid - 1
        return best
