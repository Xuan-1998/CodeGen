def solution():
    s = input().strip()
    dp = [[False, False] for _ in range(len(s) + 1)]

    for i in range(2, len(s) + 1):
        if i % 2 == 0:
            if s[i-2:i] == "AB":
                dp[i][0] = True
            elif s[i-2:i] == "BA":
                dp[i][1] = True

        else:
            dp[i][0] = dp[(i-1)//2][0]
            dp[i][1] = dp[(i-1)//2][1]

    return 'YES' if dp[-1][0] and dp[-1][1] else 'NO'

print(solution())
