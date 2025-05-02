class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i] = [tasks[i][1], i, tasks[i][0]]
        tasks.sort(reverse=True, key=lambda x: x[2])
        heap = [tasks.pop()]
        while tasks:
            if heap[0][2] == tasks[-1][2]:
                heappush(heap, tasks.pop())
            else:
                break
        result = []
        
        time = 0
        while heap:
            p, i, e = heappop(heap)
            time = max(time+p, e+p)
            while tasks and tasks[-1][2] <= time:
                heappush(heap, tasks.pop())
            result.append(i)
            if not heap and tasks:
                heappush(heap, tasks.pop())
        
        return result
          