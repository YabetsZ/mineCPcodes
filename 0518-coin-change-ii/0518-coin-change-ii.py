class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        c = len(coins)
        dp = [[0]*(amount + 1) for _ in range(c)]
        dp[0][0] = 1
        
        for i in range(c):
            for j in range(amount+1):
                cur_coin = coins[i]
                if cur_coin + j <= amount:
                    dp[i][j+cur_coin] += dp[i][j]
                if i + 1 < c:
                    dp[i+1][j] += dp[i][j]

        return dp[-1][-1]