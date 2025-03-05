# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, part = [int(x) for x in input().split()]

nums = [int(x) for x in input().split()]

sorted_diff = sorted([nums[i] - nums[i-1] for i in range(1, len(nums))])
# print(sorted_diff)
k = len(sorted_diff)
print(sum(sorted_diff[:k - part + 1]))