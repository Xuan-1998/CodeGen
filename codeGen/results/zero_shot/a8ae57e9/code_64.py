import sys

n = int(sys.stdin.readline())
requests = []
for _ in range(n):
    size, amount = map(int, sys.stdin.readline().split())
    requests.append((size, amount))

k = int(sys.stdin.readline())
max_capacity = int(sys.stdin.readline())

requests.sort(key=lambda x: x[1] / x[0], reverse=True)

accepted_requests = 0
total_amount_earned = 0

for i, (size, amount) in enumerate(requests):
    while accepted_requests < k and size <= max_capacity:
        total_amount_earned += amount
        accepted_requests += 1

table_assignments = []
for i in range(accepted_requests):
    table_assignments.append((i, 0))

print(accepted_requests, total_amount_earned)

for i in range(accepted_requests):
    print(i + 1, table_assignments[i][0])
