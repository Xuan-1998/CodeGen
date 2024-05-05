def tableways(N, M):
    MOD = 10**9 + 7
    memo = {0: 1}
    
    def dp(n_rows, prev_row_sum):
        if n_rows > N or prev_row_sum >= M:
            return 1
        
        total_sum = sum(range(M)) + prev_row_sum - M
        if (n_rows-1) in memo:
            ways = memo[(n_rows-1)]
        else:
            ways = dp(n_rows-1, M)
            memo[(n_rows-1)] = ways
            
        res = 0
        for i in range(M):
            new_row_sum = prev_row_sum + i - (total_sum-i) // (n_rows-1)
            if new_row_sum <= M:
                res += ways * ((M-new_row_sum) % MOD)
            else:
                break
        
        return res % MOD
    
    return dp(N, 0)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(tableways(N, M))
