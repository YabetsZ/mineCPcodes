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
        def comb(start, end, arr):
            if len(arr) == k:
                sol.append(arr[:])
                return
            
            for i in range(start, end+1):
                arr.append(i)
                comb(i+1, end, arr)
                arr.pop()
            
        # tryAll(1, [])
        comb(1, n, [])
        return sol