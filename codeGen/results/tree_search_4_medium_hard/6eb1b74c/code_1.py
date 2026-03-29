import sys

def solve():
    n = int(input())
    t = input()
    s = [input() for _ in range(n)]
    
    dp = [[-1] * (n + 1) for _ in range(len(t) + 1)]

    # Base case
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, len(t) + 1):
        for j in range(min(i, n) + 1):
            if dp[i - 1][j] != -1:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + (any(s[k] in t[:i] for k in range(j)) and j > 0))

    m = len(t)
    used_strings = []
    while m > 0:
        for j in range(n, -1, -1):
            if dp[m][j] != -1 and ((m - dp[m][j]) < m or not any(s[k] in t[:m-dp[m][j]] for k in range(j))):
                print(j, m - dp[m][j])
                used_strings.append(j)
                m -= dp[m][j]
                break

    if len(used_strings) == 0:
        print(-1)

if __name__ == "__main__":
    solve()
