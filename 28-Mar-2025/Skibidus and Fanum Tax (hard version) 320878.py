# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

import bisect
t = int(input())
 
def solve():
    n, m = [int(x) for x in input().split()]
 
    arr = [int(x) for x in input().split()]
    brr = [int(x) for x in input().split()]
    brr.sort()
    arr[0] = min(arr[0], brr[0]-arr[0])
 
    for i in range(1, n):
        # find the ideal index for our element in arr[i]
        ideal = bisect.bisect_left(brr, arr[i]+arr[i-1])
        if ideal < m:
            choice = min(brr[ideal] - arr[i], arr[i])
            nonchoice = max(brr[ideal] - arr[i], arr[i])
            if arr[i-1] <= choice:
                arr[i] = choice
            elif arr[i-1] <= nonchoice:
                arr[i] = nonchoice
            else:
                return "NO"
        else:
            if arr[i-1] > arr[i]:
                return "NO"
    return "YES"
 
 
for _ in range(t):
    print(solve())
