===BEGIN SOLUTION===
n = int(input())  # number of monsters
dp = [float('inf')] * (10**9 + 1)  # dynamic programming dictionary
for _ in range(n):
    k, h = map(int, input().split())  # monster appearance time and health
    for i in range(k+1):
        if i <= k:
            dp[i] = min(dp.get(i-1, float('inf')), max(h - (i-h), 0)) + 1
print(max(dp[:]))  # maximum mana required to kill all monsters
===END SOLUTION===
