# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        # print(path)
        for folder in path:
            if folder != "":
                if folder == ".":
                    continue
                elif folder == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(folder)
        return "/" + "/".join(stack)