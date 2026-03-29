def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i == 0:
                return True
            
            prev_val = None
            for k in range(j+1):
                if a[k] != b[i-1]:
                    return False
                
                if k > 0 and a[k-1] == a[k]:
                    continue
                
                prev_val = a[k]
                
            res = dfs(i-1, j)
            if not res:
                return False
            
            for k in range(j+1):
                if a[k] != b[i-1]:
                    return False
            dp[(i, j)] = True
            return True
        
        a = []
        prev_val = None
        for x in b:
            while len(a) and a[-1] == x:
                a.pop()
            
            if prev_val is not None and x != prev_val+1:
                a.append(x)
            
            prev_val = x
            
        if a[0] != 1:
            print("NO")
            continue
        
        res = dfs(n, len(a))
        if res:
            print("YES")
        else:
            print("NO")

solve()
