class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        MIN = 3*10**4 #the max allowed range: num2[i]-nums1[i]+diff
        BIT = [0]*(2*MIN + 1)
        def update(val):
            val += MIN + 1
            while val < len(BIT):
                BIT[val] += 1
                val += val & -val
        def sum(val):
            val += MIN + 1
            result = 0
            while val > 0:
                if not 0<= val <= len(BIT)-1:
                    print(val)
                result += BIT[val]
                val -= val & -val
            return result
        
        arr = [nums2[p] - nums1[p] for p in range(len(nums1))]
        count = 0
        for i in range(len(arr)-1, -1, -1):
            count += sum(arr[i]+diff)
            update(arr[i])
    
        return count