import sys

def solve():
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))

    dp = {0: 0}
    last_monster_time = 0

    for i in range(n):
        while k[i] > last_monster_time:
            if not any(t <= last_monster_time for t in dp):
                return -1
            last_monster_time += 1
            dp[last_monster_time] = min(dp.get(last_monster_time, float('inf')), dp.get(last_monster_time-1, 0) + h[i])

    return dp[last_monster_time]

t = int(input())
for _ in range(t):
    print(solve())
