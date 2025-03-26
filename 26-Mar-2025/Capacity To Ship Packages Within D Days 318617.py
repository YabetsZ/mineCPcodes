# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def countDays(test):
            count, sum_ = 1, 0
            for weight in weights:
                if sum_ + weight > test:
                    sum_ = weight
                    count += 1
                else:
                    sum_ += weight
            return count
        left, right = max(weights), sum(weights)
        result = -1
        while left <= right:
            mid = left + (right - left)//2
            resultDays = countDays(mid)
            if resultDays > days:
                left = mid + 1
            else:
                result = mid
                right = mid - 1
        return result