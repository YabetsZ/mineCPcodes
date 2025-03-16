# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [x for x in range(1, n +1)]
        def find(k, i):
            # remove based on the index
            if len(players) == 1:
                return players[0]
            remove = (i + k - 1) % len(players)
            # print(remove, players)
            players.pop(remove)
            # print(players)
            return find(k, remove % len(players))
        
            
        return find(k, 0)

        