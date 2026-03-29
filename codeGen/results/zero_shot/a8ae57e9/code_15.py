import sys

n = int(input())
requests = []
for _ in range(n):
    ci, pi = map(int, input().split())
    requests.append((ci, pi))

k = int(input())

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_amount_earned = 0
table_assignments = []

for request in requests:
    ci, pi = request
    for table in range(k):
        if ci <= k - table:
            accepted_requests += 1
            total_amount_earned += pi
            table_assignments.append((accepted_requests, table + 1))
            break

print(accepted_requests, total_amount_earned)

for i, (request_index, table_index) in enumerate(table_assignments):
    print(request_index, table_index)
