from collections import defaultdict

def solve(n, k, requests):
    dp = [[0, 0] for _ in range(k + 1)]
    
    d = {}
    s = [0] * (n + 1)
    t = [float('inf')] * (k + 1)

    for i in range(1, n + 1):
        size, money = requests[i - 1]
        s[i] = s[i - 1] + money
        if size not in d:
            d[size] = t[0]
        else:
            t[min(size, k)] = min(t[min(size, k)], d[size])
    
    for i in range(1, n + 1):
        size, money = requests[i - 1]
        max_money = s[i]
        for j in range(k, 0, -1):
            if s[i] <= dp[j][t[j]]:
                dp[j][t[j]] = max(dp[j][t[j]], s[i])
                break
        else:
            dp[0][k] = 0
    
    m = 0
    k_max = 0
    for i in range(k + 1):
        if dp[i][t[i]] > m:
            m = dp[i][t[i]]
            k_max = i
    
    print(m, k_max)
    
    accepted_requests = []
    for i in range(1, n + 1):
        size, money = requests[i - 1]
        if s[i] <= m and t[size] == t[min(size, k)]:
            accepted_requests.append((i, min(size, k)))
    
    for request in accepted_requests:
        print(*request)

requests = []
for _ in range(n):
    size, money = map(int, input().split())
    requests.append((size, money))

k = int(input())
print(solve(n, k, requests))
