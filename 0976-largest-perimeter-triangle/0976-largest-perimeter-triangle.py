class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        result = 0
        window = sum(nums[:3])
        if (nums[0] + nums[1] > nums[2] and
            nums[0] + nums[2] > nums[1] and 
            nums[1] + nums[2] > nums[0]):
            return max(result, window)
        left = 0

        for right in range(3, len(nums)):
            window += nums[right] - nums[left]

            left += 1
            i, j, k = left, left+1, left+2
            if (nums[i] + nums[j] > nums[k] and 
            nums[i] + nums[k] > nums[j] and 
            nums[j] + nums[k] > nums[i]):
                return max(result, window)
        return result