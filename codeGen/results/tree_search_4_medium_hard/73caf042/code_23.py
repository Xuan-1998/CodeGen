def solve():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                even_sum = sum(int(digit) for digit in str(i+j-1) if int(digit) % 2 == 0)
                odd_sum = sum(int(digit) for digit in str(i+j-1) if int(digit) % 2 != 0)
                
                dp[i][j] = abs(even_sum - odd_sum) + dp[i-1][j-1]
        
        print(dp[N][N])

if __name__ == "__main__":
    solve()
