class Solution:
    def numRabbits(self, ans: List[int]) -> int:
        ans.sort()
        cur = ans[0]
        count = ans[0] + 1
        result = ans[0] + 1
        for i in range(len(ans)):
            if count > 0 and ans[i] == cur:
                count -= 1
            else:
                cur = ans[i]
                count = ans[i]
                result += ans[i] + 1
        return result