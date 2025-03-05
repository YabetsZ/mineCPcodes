# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        current = []
        for log in logs:
            if log == "../":
                if current:
                    current.pop()
            elif log != "./":
                current.append(log)
        return len(current)