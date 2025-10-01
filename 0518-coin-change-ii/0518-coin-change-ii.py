class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        @cache
        def dp(i, rem):
            if rem == 0:
                return 1
            if i >= len(coins) or rem < coins[i]:
                return 0

            take = dp(i, rem-coins[i])
            not_take = dp(i+1, rem)
            return take + not_take
        
        return dp(0, amount)