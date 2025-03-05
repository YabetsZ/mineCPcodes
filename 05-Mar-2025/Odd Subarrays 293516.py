# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())

for _ in range(t):
    n = int(input())

    nums = [int(x) for x in input().split()]
    result = 0
    count = 1
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            count += 1
        else:
            result += count//2
            count = 1
    print(result + count//2)