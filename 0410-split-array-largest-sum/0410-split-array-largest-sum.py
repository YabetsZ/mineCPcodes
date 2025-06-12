class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def calculate_splits(val):
            largest_sum = -float("inf")
            sum_, splits = 0, 1
            for num in nums:
                sum_ += num
                if sum_ > val:
                    largest_sum = max(largest_sum, sum_-num)
                    sum_ = num
                    splits += 1
            largest_sum = max(largest_sum, sum_)
            return splits, largest_sum

        left, right = max(nums), sum(nums)
        best = None
        while left <= right:
            mid = left + (right-left)//2
            splits, largest_sum = calculate_splits(mid)
            print(left, right)
            if splits > k:
                left = mid + 1
            else:
                best = largest_sum
                right = mid - 1
        
        return best
