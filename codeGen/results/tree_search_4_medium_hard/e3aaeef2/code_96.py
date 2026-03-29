def solve():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = len(str(i))
        
        for ops in range(1, m + 1):
            for num in range(1, n + 1):
                if ops > 0:
                    next_num = int(''.join(map(str, (int(digit) + 1) % 10 for digit in str(num))))
                    dp[num][ops] = min(dp[num][ops - 1], dp[next_num][ops - 1]) + 1
                else:
                    dp[num][ops] = dp[num][ops - 1]
        
        print((dp[n][m]) % (10**9+7))

if __name__ == "__main__":
    solve()
