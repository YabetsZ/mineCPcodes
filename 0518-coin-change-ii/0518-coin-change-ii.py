class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        c = len(coins)
        dp = [0]*(amount + 1)
        dp[0] = 1
        
        for i in range(c):
            dp_next = [0]*(amount + 1)
            for j in range(amount+1):
                cur_coin = coins[i]
                if cur_coin + j <= amount:
                    dp[j+cur_coin] += dp[j]
                if i + 1 < c:
                    dp_next[j] += dp[j]
            if i + 1 < c:
                dp = dp_next

        return dp[-1]