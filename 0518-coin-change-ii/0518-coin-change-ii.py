class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        c = len(coins)
        dp = [0]*(amount + 1)
        dp[0] = 1
        
        for i in range(c):
            for j in range(amount+1):
                cur_coin = coins[i]
                if cur_coin + j <= amount:
                    dp[j+cur_coin] += dp[j]

        return dp[-1]