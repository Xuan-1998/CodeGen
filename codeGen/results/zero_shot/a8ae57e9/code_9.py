import sys

n, k = map(int, sys.stdin.readline().split())
requests = []
for _ in range(n):
    c, p = map(int, sys.stdin.readline().split())
    requests.append((c, p))

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_amount_earned = 0
table_capacities = [0] * k

for c, p in requests:
    for i in range(k):
        if table_capacities[i] + c <= 1000:
            table_capacities[i] += c
            accepted_requests += 1
            total_amount_earned += p
            print(f"{accepted_requests} {i+1}")
            break

print(accepted_requests)
print(total_amount_earned)
