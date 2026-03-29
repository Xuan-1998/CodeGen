n = int(input())
requests = []
for _ in range(n):
    size, amount = map(int, input().split())
    requests.append((size, amount))

k = int(input())
c = int(input())

requests.sort(key=lambda x: x[1], reverse=True)

total_earned = 0
accepted_requests = 0

tables = [[0, 0] for _ in range(k)]

for size, amount in requests:
    for i, table in enumerate(tables):
        if table[0] + size <= c:
            tables[i][0] += size
            tables[i][1] += amount
            total_earned += amount
            accepted_requests += 1
            print(f"{accepted_requests} {i+1}")
            break

print(accepted_requests)
print(total_earned)
