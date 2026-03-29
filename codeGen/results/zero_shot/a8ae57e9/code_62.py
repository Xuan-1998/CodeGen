import sys

n, k = map(int, sys.stdin.readline().split())
requests = []
for _ in range(n):
    requests.append(list(map(int, sys.stdin.readline().split())))
max_capacity_per_table = int(sys.stdin.readline())

requests.sort(key=lambda x: x[1])

accepted_requests = 0
total_earned = 0
table_assignments = {}
for request in requests:
    group_size, total_amount = request
    for table in range(k):
        if len(table_assignments.get(table, [])) < max_capacity_per_table:
            table_assignments.setdefault(table, []).append(group_size)
            accepted_requests += 1
            total_earned += total_amount
            break

print(accepted_requests, total_earned)
for i, request in enumerate(requests):
    for j, group_size in enumerate(table_assignments[i]):
        print(i+1, j+1)
