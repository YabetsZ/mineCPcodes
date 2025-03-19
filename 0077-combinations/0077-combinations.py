class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        def tryAll(cur,arr, n = n, k= k):
            if len(arr) == k:
                sol.append(arr.copy())
                return
            elif cur > n:
                return
            arr.append(cur)
            tryAll(cur+1, arr)
            arr.pop()
            tryAll(cur+1, arr)
        tryAll(1, [])
        return sol