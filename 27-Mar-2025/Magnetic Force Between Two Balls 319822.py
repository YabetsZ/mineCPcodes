# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        def check(target, m):
            count = 1
            last_num = pos[0]
            for num in pos:
                if num - last_num >= target:
                    count += 1
                    last_num = num
            return count >= m
        left, right = 0, pos[-1] - pos[0]
        best = 0
        while left <= right:
            mid = left + (right - left)//2
            if check(mid, m):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        return best
        