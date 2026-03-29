MOD = 998244353
N = int(input())
D = list(map(int, input().split()))
if D[0] != 1:
    print(0)
    exit()
D = [0] + D
cnt = [0] * (N + 1)
for i in range(1, N + 1):
    cnt[D[i]] += 1
dp = [1] + [0] * N
ans = 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] * cnt[i - 1] % MOD
    ans = ans * dp[i] % MOD
print(ans)

