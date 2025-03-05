# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, ans: List[int]) -> int:
        ans.sort()
        cur = ans[0]
        count = cur + 1
        result = cur + 1
        for num in ans:
            if count > 0 and num == cur:
                count -= 1
            else:
                cur = num
                count = num
                result += num + 1
        return result