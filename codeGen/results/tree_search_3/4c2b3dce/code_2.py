code
import sys

def solve(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n - 1):
        if s[i:i+2] == "AB":
            for j in range(i+3, n + 1):
                if s[j-1:j+1] == "BA" and s[i+2:j-1].find("AB") == -1:
                    dp[i][j] = True

    return "YES" if dp[0][n] else "NO"

if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
