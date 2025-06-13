class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def min_dist(i, j, n):
            """
            min distance between two indices in a circular array
            """
            cw = (j - i + n) % n
            ccw = (i - j + n) % n
            return min(cw, ccw)

        hashmap = defaultdict(list)
        for i in range(len(ring)):
            hashmap[ring[i]].append(i)

        def dfs(target, idx): # target: target index
            if target >= len(key):
                return 0
            result = float("inf")
            for jdx in hashmap[key[target]]:
                distance = dfs(target+1, jdx) + min_dist(idx, jdx, len(ring)) + 1 # + 1 for pressing
                result = min(result, distance)
            return result
        
        return dfs(0, 0)
