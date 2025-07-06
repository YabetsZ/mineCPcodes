class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort()
        for left, right in intervals:
            if not heap or left <= heap[0]:
                heappush(heap, right)
            else:
                heapreplace(heap, right)
        
        return len(heap)