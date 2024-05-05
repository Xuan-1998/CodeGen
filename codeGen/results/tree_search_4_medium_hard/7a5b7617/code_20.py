def solve():
    T = int(input())
    MOD = 10**9 + 7
    
    memo = {}
    
    def dp(n_rows, m_cols):
        if (n_rows, m_cols) in memo:
            return memo[(n_rows, m_cols)]
        
        if n_rows == 0:
            return 1
        
        prev_sum = sum(range(1, n_rows + 1))
        ans = 0
        for i in range(m_cols):
            ans += (prev_sum * (i + 1) + 1) % MOD
        
        memo[(n_rows, m_cols)] = ans
        return ans
    
    for _ in range(T):
        N, M = map(int, input().split())
        print(dp(N, M))

if __name__ == "__main__":
    solve()
