class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(remainder, memo=None):
            if memo is None:
                memo = {0: 0}
            elif remainder < 0:
                return float("inf")
            if remainder in memo:
                return memo[remainder]
            
            result = float("inf")
            for coin in coins:
                result = min(result, dp(remainder-coin, memo))
            
            memo[remainder] = result + 1
            return memo[remainder] 
        
        result = dp(amount)
        return result if result != float("inf") else -1