class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(reverse=True)
        heap = []
        prefix = [0] * (len(nums)+1)
        for i, num in enumerate(nums):
            prefix[i] += prefix[i-1] if i > 0 else 0

            while queries and queries[-1][0] == i:
                left, right = queries.pop()
                heappush(heap, -right)

            while prefix[i] < num and heap and -heap[0] >= i:
                prefix[i] += 1
                prefix[-heappop(heap) + 1] -= 1
            
            if prefix[i] < num:
                return -1
        
        return len(heap)