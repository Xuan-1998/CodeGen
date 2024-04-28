def solve():
    n = int(input())
    s = input()
    
    dp = {}
    def recolor(i, p):
        if (i, p) in dp:
            return dp[(i, p)]
        
        if i == 0:
            return p == 0
        
        if p < 1:
            return False
        
        res = False
        for k in range(p + 1):
            if recolor(i - 1, k) and (s[i-1] != s[i-2]) or k == 0:
                res = True
                break
        
        dp[(i, p)] = res
        return res
    
    if not recolor(n, n):
        print(-1)
    else:
        t = list(s)
        for i in range(1, n):
            if s[i-1] == s[i]:
                t[i] = 'G' if s[i-1] == 'R' else 'B'
        
        print(len([i for i, c in enumerate(t) if c != s[i]]))
        print(''.join(t))

solve()
