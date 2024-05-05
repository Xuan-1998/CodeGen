def solve():
    n = int(input())
    s = input()

    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(i+1, n+1):
            if j-i == 0 or j-i == 1:
                dp[i][j] = s[i:j]
            else:
                max_or = 0
                for k in range(i+1, j):
                    or_val = int(s[k:j], 2) | int(s[:k], 2)
                    if or_val > max_or:
                        max_or = or_val
                dp[i][j] = bin(max_or)[2:]

    return max(dp[-1])

print(solve())
