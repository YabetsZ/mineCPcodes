class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        colorRect = defaultdict(lambda: [float('inf'), float('inf'), float('-inf'), float('-inf')])

        for i in range(len(targetGrid)):
            for j in range(len(targetGrid[0])):
                color = targetGrid[i][j]
                colorRect[color][0] = min(colorRect[color][0], i)
                colorRect[color][1] = min(colorRect[color][1], j)
                colorRect[color][2] = max(colorRect[color][2], i)
                colorRect[color][3] = max(colorRect[color][3], j)

        graph = defaultdict(set)

        for color in colorRect:
            iStart, jStart, iEnd, jEnd = colorRect[color]
            for i in range(iStart, iEnd+1):
                for j in range(jStart, jEnd+1):
                    if targetGrid[i][j] != color:
                        graph[color].add(targetGrid[i][j])

        colorState = defaultdict(int)

        def hasCycle(v):
            colorState[v] = 1
            for u in graph[v]:
                if colorState[u] == 1 or ((u not in colorState or colorState[u] == 0) and hasCycle(u)):
                    return True
            colorState[v] = 2
            return False

        return not any(hasCycle(n) for n in range(1, 61) if n not in colorState or colorState[n] == 0)
