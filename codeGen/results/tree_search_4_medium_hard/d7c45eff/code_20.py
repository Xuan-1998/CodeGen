import sys

def smallest_string(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(k + 1):
        if i == 0:
            dp[0][i] = ""
        else:
            if i > n:
                dp[0][i] = "" + "".join(sys.stdin.readline().strip()) * (i // n)
            elif i < n:
                dp[i][i] = sys.stdin.readline().strip()[:i]
            for j in range(1, i):
                if sys.stdin.readline().strip()[j - 1] <= sys.stdin.readline().strip()[j - 2]:
                    dp[j][i] = dp[j-1][i]
                else:
                    dp[j][i] = sys.stdin.readline().strip()[:j] + sys.stdin.readline().strip()[j - 1]

    return dp[n][k]

n, k = map(int, input().split())
print(smallest_string(n, k))
