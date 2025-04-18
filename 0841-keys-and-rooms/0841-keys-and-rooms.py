class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        count = 1
        queue = deque([0])
        opened = set([0])
        while queue:
            room = queue.popleft()
            for roomKey in rooms[room]:
                if roomKey not in opened:
                    opened.add(roomKey)
                    queue.append(roomKey)
        return len(opened) == len(rooms)
