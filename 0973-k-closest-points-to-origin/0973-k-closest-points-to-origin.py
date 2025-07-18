class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heappush(heap, [(x**2 + y**2)**0.5, x, y])
        
        return [[x, y] for _, x, y in nsmallest(k, heap)]