# Problem: E - Strange Mirroring - https://codeforces.com/gym/596141/problem/E

t = int(input())
import math
def find(l, q, count):
    if q <= l:
        return (q, count)
 
    exp = math.ceil(math.log(q/l, 2) - 1)
 
    return find(l, q-(l*2**exp), count+1)
 
 
 
 
for _ in range(t):
    s = input()
    n = int(input()) # number of queries
 
    queries = [int(x) for x in input().split()]
 
    result = []
    for q in queries:
        idx, count = find(len(s), q, 0)
        if count%2:
            result.append(s[idx-1].swapcase())
        else:
            result.append(s[idx-1])
    
 
    print(*result)