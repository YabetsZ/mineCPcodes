class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        sortedArrival = sorted(times, key=lambda x: x[0])
        result = {}
        heap = []
        for i in range(len(times)):
            arr, des = sortedArrival[i]
            if  heap and heap[0] <= arr:
                while heap:
                    heappop(heap)
                    if not heap or heap[0] > arr:
                        break
            heappush(heap, des)    
            result[(arr, des)] = len(heap)-1
        arr, des = times[targetFriend]
        return result[(arr, des)]