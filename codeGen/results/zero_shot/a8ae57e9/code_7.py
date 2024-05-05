import sys

n, k = map(int, input().split())
requests = []
for _ in range(n):
    ci, pi = map(int, input().split())
    requests.append((ci, pi))

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_earned = 0
table_assignments = []

tables = [0] * k

for request in requests:
    ci, pi = request
    for i in range(k):
        if tables[i] + ci <= k:
            tables[i] += ci
            table_assignments.append((accepted_requests + 1, i))
            accepted_requests += 1
            total_earned += pi
            break

print(accepted_requests, total_earned)
for assignment in table_assignments:
    print(*assignment)
