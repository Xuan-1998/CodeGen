from collections import defaultdict
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

requests = []
for _ in range(n):
    size, amount = map(int, input().split())
    requests.append((size, amount))

requests.sort()

max_earnings = 0
accepted_requests = 0

tables = defaultdict(int)
for i, (size, amount) in enumerate(requests):
    while tables[k] >= size and k > 0:
        dp[i][k] = max(dp[i-1][max(0, amount - requests[i-1][1])], 0) + size
        accepted_requests += 1
        max_earnings += size
        tables[k] -= size
        k -= 1

print(max_earnings)
print(accepted_requests)
for i in range(n):
    if dp[i][k] > dp[i-1][max(0, requests[i][1])]:
        print(i+1, k+1)
