class Solution:
    def numRabbits(self, ans: List[int]) -> int:
        ans.sort()
        cur = ans[0]
        count = ans[0] + 1
        result = ans[0] + 1
        for num in ans:
            if count > 0 and num == cur:
                count -= 1
            else:
                cur = num
                count = num
                result += num + 1
        return result