import heapq

# Read inputs from stdin
n, k, c = [int(x) for x in input().split()]
requests = []
for _ in range(n):
    size, spent = map(int, input().split())
    requests.append((size, spent))

requests.sort(key=lambda x: x[1], reverse=True)

dp = [[0] * (c + 1) for _ in range(k + 1)]
tables = [i for i in range(c + 1)]

for size, spent in requests:
    while tables and spent > 0:
        table_size = heapq.heappop(tables)
        if table_size >= size:
            dp[k - len(tables)][spent] += spent
            spent -= size * (k - len(tables))
            break

print(dp[-1][-1])
