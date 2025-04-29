class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        N = len(nums)-1
        def heap_down(n, cur): # here n is the length of the array
            temp = cur
            leftChild, rightChild = 2*cur+1, 2*cur+2
            if leftChild < n and nums[leftChild] > nums[temp]:
                temp = leftChild
            if rightChild < n and nums[rightChild] > nums[temp]:
                temp = rightChild
            
            if temp != cur:
                nums[temp], nums[cur] = nums[cur], nums[temp]
                heap_down(n, temp)
        for i in range((N-1)//2, -1, -1):
            heap_down(N+1, i)
        for i in range(N+1):
            if i+1 == k:
                return nums[0]
            nums[0], nums[N-i] = nums[N-i], nums[0]
            heap_down(N-i, 0)


