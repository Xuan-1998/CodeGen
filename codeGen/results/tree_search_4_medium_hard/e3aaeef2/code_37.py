def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(m + 1):
                if j == 0:
                    dp[i][j] = i
                elif i == 1:
                    dp[i][j] = 1
                else:
                    last_digit_even = False
                    new_length = dp[i-1][j-1]
                    for k in range(10):
                        if (k + 1) % 2 != 0:  # even number
                            last_digit_even = True
                            break
                    if not last_digit_even:
                        new_length += 1
                    
                    dp[i][j] = min(new_length, dp[i-1][j])
        
        print(dp[n][m] % (10**9 + 7))

if __name__ == "__main__":
    solve()
