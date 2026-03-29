def min_changes():
    n, k = map(int, input().split())
    s = input()

    dp = [[False] * 3 for _ in range(n + 1)]

    dp[0][0] = True

    changes = 0

    for i in range(1, n + 1):
        if s[i - 1] != 'R':
            dp[i][0] = dp[i - 1][1]
        else:
            dp[i][0] = False
        if s[i - 1] != 'G':
            dp[i][1] = dp[i - 1][2]
        else:
            dp[i][1] = False
        if s[i - 1] != 'B':
            dp[i][2] = dp[i - 1][0]
        else:
            dp[i][2] = False

    for i in range(k):
        changes += int(dp[k - 1][i] and not (s[k - 1] == 'R' and i % 3 == 0) 
                         and not (s[k - 1] == 'G' and i % 3 == 1) 
                         and not (s[k - 1] == 'B' and i % 3 == 2))

    print(changes)
