def dp(i, j):
    if i == 1 or j == 0:
        return 1
    ans = 0
    for k in range(max(0, M - (j-1) * i) + 1):
        ans += dp(i-1, j-1)
    return ans % 1000000000

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(dp(N, M))
