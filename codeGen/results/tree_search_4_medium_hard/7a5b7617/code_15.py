import sys

def count_steady_tables(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, m + 1):
            if j < i:
                dp[i][j] = 0
            else:
                dp[i][j] = (sum(range(j - i + 1)) % 1000000000) * (m - j + 1)

    return dp[n][m]

def main():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        print(count_steady_tables(n, m))

if __name__ == "__main__":
    main()
