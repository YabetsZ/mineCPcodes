class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def check(idx):
            arr = [0]*(len(nums)+1)
            for i in range(idx+1):
                l, r, val = queries[i]
                arr[l] += val
                arr[r+1] -= val
            for i in range(1, len(arr)):
                arr[i] += arr[i-1]
            for i in range(len(nums)):
                if arr[i] < nums[i]:
                    return False
            return True
        left, right = 0, len(queries)-1
        best = -1
        while left <= right:
            mid = left + (right-left)//2
            possible = check(mid)
            if possible:
                best = mid + 1
                right = mid - 1
            else:
                left = mid + 1
        return best
        