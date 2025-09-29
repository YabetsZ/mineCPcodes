class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stones_dict = {stone: index for (index, stone) in enumerate(stones)}
        
        def dp(prev_step, pos, memo=None):
            if memo is None: memo = {}
            if pos == 0:
                return stones[1] == 1 and dp(1, 1)
            if pos == len(stones)-1:
                return True
            elif pos >= len(stones):
                return False
            
            if (prev_step, pos) in memo:
                return memo[(prev_step, pos)]

            for i in [-1, 0, 1]:
                new_step = prev_step + i
                if new_step == 0: continue
                stone = stones[pos] + new_step
                if stone in stones_dict and dp(new_step, stones_dict[stone], memo):
                    memo[(prev_step, pos)] = True
                    return True

            memo[(prev_step, pos)] = False
            return False

        return dp(1, 0)
