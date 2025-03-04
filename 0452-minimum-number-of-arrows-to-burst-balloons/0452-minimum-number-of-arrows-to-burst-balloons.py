class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        count = 1
        print(points)
        lim = points[0][1]
        for i in range(1, len(points)):
            pt = points[i]
            if lim < pt[0]:
                count += 1
                lim = pt[1]
                continue
            else:
                lim = min(lim, pt[1])
        return count
