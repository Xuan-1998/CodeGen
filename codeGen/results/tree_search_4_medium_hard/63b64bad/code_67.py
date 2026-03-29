n = int(input())
DP = [-1] * (n + 1)
a = list(map(int, input().split()))

for x in range(1, n):
    next_state_x = min(x + a[x - 1], n - 1)
    DP[next_state_x] = DP[x - 1] + a[x - 1]

for i in range(2, n + 1):
    print(DP[i - 1])
