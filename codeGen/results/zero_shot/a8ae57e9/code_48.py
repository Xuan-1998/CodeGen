import sys

n = int(input())
requests = []
for _ in range(n):
    ci, pi = map(int, input().split())
    requests.append((ci, pi))

k = int(input())
ri = int(input())

accepted_requests = 0
total_earned = 0
table_assignments = []

requests.sort(key=lambda x: x[1], reverse=True)

for i, (ci, pi) in enumerate(requests):
    if ci <= k:
        accepted_requests += 1
        total_earned += pi
        table_assignments.append((i, ri))
        ri -= ci

print(accepted_requests)
print(total_earned)

for assignment in table_assignments:
    print(*assignment)
