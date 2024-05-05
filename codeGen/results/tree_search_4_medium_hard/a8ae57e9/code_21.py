import sys

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
s = [0] * (n + 1)
t = [0] * (n + 1)

requests = []
for _ in range(n):
    r, p = map(int, input().split())
    requests.append((r, p))

requests.sort(reverse=True)

for i, (r, p) in enumerate(requests, 1):
    s[i] = s[i - 1] + p
    for j in range(k, -1, -1):
        if s[i] > dp[i][j]:
            t[i] = j
            break

print(s[n], len([p for p in requests if p[1] >= s[n]][0]))

accepted_requests = [p for p in requests if p[1] >= s[n]]
accepted_requests.sort(reverse=True)

for i, (r, p) in enumerate(accepted_requests, 1):
    print(i, t[r])
