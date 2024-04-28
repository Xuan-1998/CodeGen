n = int(input())
a = list(map(int, input().split()))
dp = {}
s = 0
for x in a:
    s += x
    for y in range(s+1):
        dp[y] = dp.get(y, 0) + (y-x if y>=x else 0)
ans = set()
for v in dp.values():
    ans.add(v)
print(*sorted(ans), sep=' ')
