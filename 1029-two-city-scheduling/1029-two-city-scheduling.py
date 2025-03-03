class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[0]-x[1]), reverse=True)

        # -1, 0, 1
        val = 0
        second = 0
        first = 0
        for arr in costs:
            if second == len(costs)//2 or arr[0] < arr[1] :
                val += arr[0]
                first += 1
            else:
                val += arr[1]
                second += 1
        return val
