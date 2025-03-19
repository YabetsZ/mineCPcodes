class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        def tryAll(cur,arr, n, k):
            if len(arr) == k:
                sol.append(arr.copy())
                return
            elif cur > n:
                return
            arr.append(cur)
            tryAll(cur+1, arr, n, k)
            arr.pop()
            tryAll(cur+1, arr, n, k)
        tryAll(1, [], n, k)
        return sol