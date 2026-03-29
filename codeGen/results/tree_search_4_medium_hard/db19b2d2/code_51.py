import math

def calculate_probability(n, m, h, s):
    dp = [[0.0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for k in range(min(i, n) + 1):
            if i == h:
                dp[i][k] = 1.0
            else:
                dp[i][k] = (dp[i - 1][min(k, s[i - 1])] + 
                            dp[i - 1][k]) / (i * (m - i))

    return dp[m][n]

def main():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    print(calculate_probability(n, m, h, s))

if __name__ == "__main__":
    main()
