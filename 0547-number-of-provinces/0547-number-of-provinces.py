class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        cities = {i: [[i]] for i in range(n)}
        provinces = set([i for i in range(n)])
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    if cities[i][0] is not cities[j][0]:
                        provinces.discard(cities[j][0][0])
                        cities[j][0] = cities[i][0]
        # print(cities)
        # if n > 12:
        #     print(isConnected[4])
        return len(provinces)

