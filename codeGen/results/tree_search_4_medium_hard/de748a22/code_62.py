n, q = map(int, input().split())
arr = list(input())

pref_sum = [0] * (n + 1)
diff_sum = [0] * (n + 1)

for i in range(1, n + 1):
    if arr[i - 1] == 1:
        pref_sum[i] = pref_sum[i - 1] + 1
    else:
        pref_sum[i] = pref_sum[i - 1] - 1

diff_sum[0] = 0
for i in range(1, n + 1):
    diff_sum[i] = diff_sum[i - 1] + (arr[i - 1] == 1) * 2 - 1

dp = [[float('inf')] * q for _ in range(n + 1)]

for i in range(q):
    l_i, r_i = map(int, input().split())
    dp[l_i][0] = (pref_sum[r_i] - pref_sum[l_i - 1]) % 2
    for j in range(1, n + 1):
        dp[j][i] = min(dp[j - 1][i], abs(diff_sum[r_i] - diff_sum[l_i - 1]))

ans = float('inf')
for i in range(n + 1):
    ans = min(ans, dp[i][q - 1])
print(ans)
