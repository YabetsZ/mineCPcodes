class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        bit_length = 2**(len(nums))-1 
        for i in range(bit_length+1):
            temp = []
            ptr, j = 0, i
            while j > 0:
                if j & 1 != 0:
                    temp.append(nums[ptr])
                j >>= 1
                ptr += 1
            result.append(temp)
        
        return result