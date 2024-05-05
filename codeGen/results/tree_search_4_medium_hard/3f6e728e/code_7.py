def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        
        dp = [0] * (C + 1)
        
        for i in range(C, 0, -1):
            for j in range(1, i):
                if len([x for x in U if x >= i]) > 0:
                    Uj = len([x for x in U if x >= i])
                else:
                    Uj = j
                
                if L[0] <= i:
                    Lj = len(L)
                else:
                    Lj = 0
                
                dp[i] = (dp[i] + (Uj * Lj) % (10**9 + 7)) % (10**9 + 7)
        
        print(*[str(dp[i]) for i in range(C)], sep=' ')

solve()
