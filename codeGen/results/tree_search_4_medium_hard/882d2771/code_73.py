def solve():
    t, l, r = map(int, input().split())
    memo = {(1,): 0}
    
    def f(n):
        if (n,) in memo:
            return memo[(n,)]
        
        if n == 2:
            return 2
        
        res = float('inf')
        for i in range(1, n//2 + 1):
            res = min(res, f(i) + f(n - i))
        
        memo[(n,)] = res
        return res
    
    print((f(r) * t) % (10**9 + 7))

if __name__ == "__main__":
    solve()
