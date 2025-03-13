# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
n, k = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

small = deque() # increasing
big = deque() # decreasing

total = 0

left = -1
for right in range(n):
    while small and arr[small[-1]] > arr[right]:
        small.pop()
    while big and arr[big[-1]] < arr[right]:
        big.pop()
        
    small.append(right)
    big.append(right)

    while arr[big[0]] - arr[small[0]] > k:
        if big[0] < small[0]:
            left = big.popleft()
        else:
            left = small.popleft()
    
    total += right - left

print(total)

