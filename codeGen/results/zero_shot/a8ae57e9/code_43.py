n = int(input())
requests = []
for _ in range(n):
    ci, pi = map(int, input().split())
    requests.append((ci, pi))
k = int(input())
max_capacity = int(input())

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_earned = 0
table_assignments = []
for ci, pi in requests:
    assigned = False
    for i in range(k):
        if len(table_assignments) <= i and table_assignments[i] + ci <= max_capacity:
            table_assignments.append((i, ci))
            accepted_requests += 1
            total_earned += pi
            assigned = True
            break
    if not assigned:
        print("Cannot accommodate the request", ci, "with", pi)

print(accepted_requests, total_earned)
for i, (ci, _) in enumerate(table_assignments):
    print(i+1, ci+1)
