def can_merge(p):
    n = len(p) // 2
    dp = [[False] * (n + 1) for _ in range(len(p) + 1)]

    for i in range(1, len(p) + 1):
        if p[i - 1] < p[n]:
            dp[i][0] = dp[i - 1][0]
        elif p[i - 1] > p[n]:
            dp[i][0] = dp[i - 1][n]
        else:
            dp[i][0] = dp[i - 2][n]

    for i in range(1, len(p) + 1):
        for j in range(1, n + 1):
            if p[i - 1] < p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[i - 1] > p[j - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 2][j - 1]

    return dp[-1][-1]


def main():
    n = int(input())
    p = list(map(int, input().split()))
    if can_merge(p):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
