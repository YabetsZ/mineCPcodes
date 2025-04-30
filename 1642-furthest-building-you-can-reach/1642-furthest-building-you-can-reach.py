class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n, sumMin = len(heights), 0
        heightForLadder = []
        for i in range(n-1):
            if heights[i] < heights[i+1]:
                difference = heights[i+1] - heights[i]
                if len(heightForLadder) < ladders:
                    heappush(heightForLadder, difference)
                else:
                    sumMin += heappushpop(heightForLadder, difference)
                    if sumMin > bricks:
                        return i
        return n-1

