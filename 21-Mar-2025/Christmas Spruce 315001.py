# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

from collections import defaultdict


n = int(input())
T = defaultdict(int)
for node in range(2, n+1):
    p = int(input())
    if p not in T:
        T[p] = []
    T[p].append(node)

# print(T)

def dfs(node):
    # if not T[node]:
    #     return 1
    count = 0
    for child in T[node]:
        if not T[child]:
            count += 1
        else:
            if not dfs(child):
                return False
    return count >= 3

print("Yes" if dfs(1) else "No")