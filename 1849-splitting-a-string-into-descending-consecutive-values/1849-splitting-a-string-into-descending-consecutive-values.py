class Solution:
    def splitString(self, s: str) -> bool:
        def split(s, arr):
            if len(s) == 0:
                return len(arr) > 1
            for i in range(1, len(s)+1):
                # print(arr)
                chopped = int(s[:i])
                if not arr or chopped < arr[-1] and arr[-1] - chopped == 1:
                    arr.append(chopped)
                    if split(s[i:], arr):
                        return True
                    arr.pop()
            return False
        return split(s, [])
                