import sys

n = int(sys.stdin.readline())
requests = []
for _ in range(n):
    ci, pi = map(int, sys.stdin.readline().split())
    requests.append((ci, pi))

requests.sort(key=lambda x: x[1] / x[0], reverse=True)

total_earned = 0
accepted_requests = 0

tables_assigned = {}
table_capacity = int(sys.stdin.readline())

for ci, pi in requests:
    if ci > table_capacity:
        continue
    accepted_requests += 1
    total_earned += pi
    for _ in range(ci):
        table_available = False
        for table, capacity in tables_assigned.items():
            if capacity >= ci:
                tables_assigned[table] -= ci
                table_available = True
                break
        if not table_available:
            continue
        print(f"{accepted_requests} {table}")
