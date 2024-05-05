n = int(input())
requests = []
for _ in range(n):
    group_size, total_amount = map(int, input().split())
    requests.append((group_size, total_amount))

k = int(input())
tables = [(0, 1) for _ in range(k)]

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_earned = 0
for request in requests:
    group_size, total_amount = request
    accepted = False
    for i, table in enumerate(tables):
        if table[1] >= group_size:
            tables[i] = (table[0], table[1] - group_size)
            accepted_requests += 1
            total_earned += total_amount
            print(f"{accepted_requests} {i+1}")
            break

print(accepted_requests, total_earned)
