class Solution:
    def smallestChair(self, times: List[List[int]], target: int) -> int:
        sortedArrival = sorted(times)
        heap, available = [], []
        for i in range(len(times)):
            arrive, leave = sortedArrival[i]
            while heap and heap[0][0] <= arrive:
                pleave, pPlace = heappop(heap)
                heappush(available, pPlace)

            appropriatePlace = heappop(available) if available else len(heap)
            if [arrive, leave] == times[target]:
                return appropriatePlace

            heappush(heap, (leave, appropriatePlace))
