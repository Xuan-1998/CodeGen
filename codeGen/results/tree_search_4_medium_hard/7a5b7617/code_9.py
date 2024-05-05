def solve():
    T = int(input())
    
    for _ in range(T):
        N, M = map(int, input().split())
        
        memo = [[0]* (M+1) for _ in range(N+1)]
        
        for j in range(M+1):
            memo[1][j] = 1
        
        for i in range(2, N+1):
            for j in range(1, M+1):
                if j <= M:
                    memo[i][j] = sum(memo[k][j-1] for k in range(i)) % (10**9 + 7)
                else:
                    prev_sum = sum(memo[k][M-1] for k in range(i))
                    if prev_sum > M:
                        memo[i][j] = (memo[i-1][M] * (2*M - j) + memo[i-1][j]) % (10**9 + 7)
                    else:
                        memo[i][j] = memo[i-1][M]
        
        print(sum(memo[N]) % (10**9 + 7))

solve()
