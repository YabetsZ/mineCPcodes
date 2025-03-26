class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.winner = []
        prev_win = self.persons[0]
        win_freq = {}
        for num in self.persons:
            win_freq[num] = win_freq.get(num, 0) + 1
            if win_freq[prev_win] <= win_freq[num]:
                prev_win = num
            self.winner.append(prev_win)
        

    def binarySearch(self, target: int) -> int:
        left, right = 0, len(self.times)-1
        while left < right:
            mid = left + (right - left)//2 + 1

            if self.times[mid] == target:
                return mid
            elif self.times[mid] > target:
                right = mid - 1
            else:
                left = mid
        return left

    def q(self, t: int) -> int:
        idx = self.binarySearch(t)
        return self.winner[idx]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)