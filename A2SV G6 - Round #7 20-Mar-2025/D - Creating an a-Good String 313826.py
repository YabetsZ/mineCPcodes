# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

t = int(input())


for _ in range(t):
    l = int(input())
    s = input()
    def calculate(l, r, char):
        count = 0
        for i in range(l, r+1):
            if s[i] != char:
                count += 1
        return count

    # 4, 5, 6, 7 
    def find(l, r, char):
        if l == r:
            if char == s[l]:
                return 0
            else:
                return 1
        
        mid = (l+r)//2 + 1
        nxt = chr(ord(char)+1)
        left = calculate(l, mid-1, char) + find(mid, r, nxt) 
        right = find(l, mid-1, nxt) + calculate(mid, r, char)

        return min(left, right)
    print(find(0, l-1, "a"))
