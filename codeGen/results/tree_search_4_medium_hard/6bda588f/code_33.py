def min_F(n, s, a):
    memo = {}
    def dfs(i, prev):
        if i >= n: return 0
        if (i, prev) in memo: return memo[(i, prev)]
        
        ans = float('inf')
        for x in range(prev+1):
            y = prev - x
            val = a[i] * x + y * (a[i-1]-s)
            if (x-s)*(y-s) >= 0:
                ans = min(ans, dfs(i+1, val))
        
        memo[(i, prev)] = ans
        return ans
    
    return dfs(1, s)

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_F(n, s, a))
