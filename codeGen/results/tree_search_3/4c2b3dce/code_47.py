def solve():
    s = input().strip()
    a, b = 0, float('inf')
    
    for i in range(len(s)):
        if s[i] == 'A':
            a = i
        elif s[i] == 'B' and i - a >= 2:
            print("YES")
            return
    
    print("NO")

solve()
