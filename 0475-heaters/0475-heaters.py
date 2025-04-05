class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # houses.sort()
        # heaters.sort()
        def verify(radius):
            i = 0
            for heat in heaters:
                while i < len(houses):
                    if not(heat-radius <= houses[i] <= heat+radius):
                        break
                    i += 1
                if i == len(houses):
                    break
            return i == len(houses)
        left, right = 0, 10**9
        best = -1
        while left <= right:
            mid = left + (right-left)//2
            if verify(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best
        