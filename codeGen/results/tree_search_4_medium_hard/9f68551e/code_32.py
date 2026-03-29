import sys

n = int(input())
for _ in range(n):
    n_monsters = int(input())
    monsters_appearance_time = list(map(int, input().split()))
    monsters_health = list(map(int, input().split()))

    dp = [[0] * (max(monsters_appearance_time) + 1) for _ in range(max(monsters_appearance_time) + 1)]

    for i in range(1, n_monsters):
        for j in range(1, monsters_appearance_time[i]):
            dp[j][j-1] = min(dp[j-1][j-2], j)

    for i in range(n_monsters - 2, -1, -1):
        for j in range(monsters_appearance_time[i]-1, -1, -1):
            if j < monsters_health[i]:
                dp[monsters_appearance_time[i]][j] = min(dp[monsters_appearance_time[i]-1][max(0, j-1)], monsters_health[i])
            else:
                dp[monsters_appearance_time[i]][j] = dp[monsters_appearance_time[i]-1][max(0, j-1)]

    print(min(dp[-1]))
