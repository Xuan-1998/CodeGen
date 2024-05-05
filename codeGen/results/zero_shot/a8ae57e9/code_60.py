import sys

n = int(sys.stdin.readline())
requests = []
for _ in range(n):
    group_size, total_amount = map(int, sys.stdin.readline().split())
    requests.append((group_size, total_amount))

k = int(sys.stdin.readline())
tables = [int(sys.stdin.readline()) for _ in range(k)]

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_amount_earned = 0
table_indices = []

for i, (group_size, total_amount) in enumerate(requests):
    found_table = False
    for j, table_capacity in enumerate(tables):
        if table_capacity >= group_size:
            tables[j] -= group_size
            accepted_requests += 1
            total_amount_earned += total_amount
            table_indices.append((i, j))
            found_table = True
            break
    if not found_table:
        print("Not enough capacity to seat all groups.")

print(accepted_requests, total_amount_earned)
for request_index, table_index in table_indices:
    print(request_index + 1, table_index + 1)
