def calculate_probability(n):
    mod = 998244353
    dp = [[False] * (n + 1) for _ in range(n + 2)]
    
    for i in range(1, n + 1):
        for j in range(min(i, n) + 1):
            if j == 0:
                dp[i][j] = True
            elif i % 2 != 0 or j == 1:
                if dp[i - 1][j - 1]:
                    dp[i][j] = True
    
    probability = 0
    for j in range(1, n + 1):
        if dp[n][j]:
            probability += 1
    return (probability % mod) * pow(mod - 1, -1, mod)

if __name__ == "__main__":
    n = int(input())
    print(calculate_probability(n))
