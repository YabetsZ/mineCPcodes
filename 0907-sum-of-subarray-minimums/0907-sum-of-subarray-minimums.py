class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        next_smaller = [n]*n
        prev_smaller = [-1]*n
        stack = []
        subarray_sum = 0
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                next_smaller[idx] = i
                # by the time any element gets popped from the stack it has both 
                #   nextSmaller and prevSmaller so we can calculate the sum of subarray minimums
                subarray_sum += arr[idx]*((next_smaller[idx] - idx) * (idx - prev_smaller[idx]))
                # subarray_sum is the number of subarrays containing arr[idx] between ns and ps indices multiplied by the element at idx.
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)
        
        while stack:
            idx = stack.pop()
            subarray_sum += arr[idx]*((next_smaller[idx] - idx) * (idx - prev_smaller[idx]))
        return subarray_sum % (10**9 + 7)
