def solve():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        memo = {1: 1}
        
        def f(i):
            if i not in memo:
                if i % 9 == 0:
                    memo[i] = f(1)
                else:
                    memo[i] = f(i % 9) + 1
            return memo[i]
        
        print(f(n) % (10**9 + 7))

solve()
