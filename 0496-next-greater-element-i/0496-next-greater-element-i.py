class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = defaultdict(lambda: -1)

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                elem = nums2[stack.pop()]
                result[elem] = nums2[i]
            stack.append(i)
        
        ans = []
        for num in nums1:
            ans.append(result[num])
        
        return ans
