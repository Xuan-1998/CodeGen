n = int(input())
a = list(map(int, input().split()))
dp = [0] * (max(a) + 1)
for i in range(len(a)):
    for j in range(min(a[i], len(a)), 0, -1):
        dp[j] = max(dp[j-1], dp[j-a[i]] + (i+1))
state = {sum(a[0]): n - sum(a[0])}
for sum_, val_ in enumerate(a):
    state[sum_] = max(state.get(sum_-1, 0), state.get(sum_-1, 0) + n - sum_)
print(max(state.values()))
