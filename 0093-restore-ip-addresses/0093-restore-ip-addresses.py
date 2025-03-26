class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def divide(s, partial):
            if len(s) + len(partial) < 4 or math.ceil(len(s)/3) + len(partial) > 4: return
            if s == "" and len(partial) == 4:
                result.append(".".join(partial))
                return

            for i in range(1, 4):
                if len(s) < i:
                    break
                candidate = s[:i]
                if int(candidate) > 255 or (candidate[0] == "0" and i > 1):
                    break
                partial.append(candidate)
                divide(s[i:], partial)
                partial.pop()
        divide(s, [])
        return result
            