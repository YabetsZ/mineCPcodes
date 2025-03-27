# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()
        def condition(time):
            count = 0
            for rank in ranks:
                count += math.floor(math.sqrt(time/rank))
                if count >= cars:
                    return True
            return False

        best = -1
        left, right = 1, max(ranks)*cars**2
        while left <= right:
            mid = left + (right-left)//2
            if condition(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best