# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())

for _ in range(t):
    rn = int(input())
    r = [int(x) for x in input().split()] 
    bn = int(input())
    b = [int(x) for x in input().split()]

    maxr, sumr = 0, 0
    for num in r:
        sumr += num
        maxr = max(maxr, sumr)
    maxb, sumb = 0, 0
    for num in b:
        sumb += num
        maxb = max(maxb, sumb)
    
    print(maxr + maxb)
