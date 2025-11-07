class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(rem, count, start):
            if rem == 0:
                result.append(count.copy())
                return count
            
            for i in range(start, len(candidates)):
                cur = candidates[i]
                if cur > rem: break
                count.append(cur)
                backtrack(rem-cur, count, i)
                count.pop()

            return count
        
        backtrack(target, [], 0)
        return result
