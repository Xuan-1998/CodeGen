from math import comb
n, m, c = map(int, input().split())
dp = [0] * (c + 1)

for _ in range(n):
    u = list(map(int, input().split()))
    for i in range(1, c + 1):
        dp[i] += comb(len([x for x in u if x == i]), len([x for x not in u if x < i]))

for _ in range(m):
    l = list(map(int, input().split()))
    for i in range(1, c + 1):
        dp[i] += comb(len([x for x in l if x == i]), len([x for x not in l if x < i]))

print(*[dp[i] % (10**9 + 7) for i in range(1, c + 1)], sep=' ')
