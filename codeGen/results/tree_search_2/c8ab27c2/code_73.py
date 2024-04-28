from io import StringIO
import sys

def get_ints():
    return list(map(int, input().split()))

def main():
    # Read input from standard input
    s = input()
    t = input()

    n = len(s)
    m = len(t)

    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = -1
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                for k in range(j):
                    if dp[i - 1][k] != -1 and dp[i - 1][k] < dp[i][j]:
                        dp[i][j] = 1 + dp[i - 1][k]

    # Print the answer to standard output
    print(dp[n][m])

if __name__ == "__main__":
    main()
