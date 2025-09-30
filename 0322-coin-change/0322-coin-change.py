class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # ITERATIVE APPROACH
        dp = [float("inf")]*(amount + 1)
        dp[0] = 0 # basecase
        for remainder in range(1, amount+1):
            for coin in coins:
                if remainder-coin < 0: continue
                dp[remainder] = min(dp[remainder], dp[remainder-coin]+1)
        
        return dp[amount] if dp[amount] != float("inf") else -1


        # RECURSIVE APPROACH (1093ms)
        # def dp(remainder, memo=None):
        #     if memo is None:
        #         memo = {0: 0}
        #     elif remainder < 0:
        #         return float("inf")
        #     if remainder in memo:
        #         return memo[remainder]
            
        #     result = float("inf")
        #     for coin in coins:
        #         result = min(result, dp(remainder-coin, memo))
            
        #     memo[remainder] = result + 1
        #     return memo[remainder] 
        
        # result = dp(amount)
        # return result if result != float("inf") else -1