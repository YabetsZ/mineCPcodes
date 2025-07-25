class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        count_p = Counter(p)
        count_s = Counter(s[: len(p) - 1])

        def check():
            for key, val in count_p.items():
                if count_s[key] != val:
                    return False
            return True

        result = []
        for right in range(len(p) - 1, len(s)):
            count_s[s[right]] += 1

            left = right - len(p) + 1
            if check():
                result.append(left)
            count_s[s[left]] -= 1

        return result
