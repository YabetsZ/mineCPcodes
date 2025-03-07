# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        n = len(deck)
        dq = deque(range(n))
        ans = [0] * n

        while dq:
            ans[dq.popleft()] = deck.pop()
            if dq:
                dq.append(dq.popleft())
        return ans
