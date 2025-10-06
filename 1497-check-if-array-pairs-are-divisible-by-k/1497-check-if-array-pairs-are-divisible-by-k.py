class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        pair_check = {}
        for num in arr:
            if num % k == 0:
                continue
            mod = num % k
            if k - mod in pair_check:
                pair_check[k-mod] -= 1
                if pair_check[k-mod] == 0:
                    del pair_check[k-mod]
            else:
                pair_check[mod] = pair_check.get(mod, 0) + 1
        
        return len(pair_check) == 0