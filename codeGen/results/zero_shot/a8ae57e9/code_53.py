import sys

n = int(sys.stdin.readline())
requests = []
for _ in range(n):
    group_size, total_amount = map(int, sys.stdin.readline().split())
    requests.append((group_size, total_amount))

k = int(sys.stdin.readline())
max_capacity = int(sys.stdin.readline())

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_earned = 0
table_assignments = []
for i, (group_size, total_amount) in enumerate(requests):
    if accepted_requests < k:  # Check if we have enough tables
        if group_size <= max_capacity:  # Check if the group fits on a table
            accepted_requests += 1
            total_earned += total_amount
            table_assignments.append((i, 0))  # Assign the request to the first available table (0-indexed)
        else:
            break  # No more tables left; stop accepting requests

print(accepted_requests, total_earned)  # Print the number of accepted requests and the total earned
for i in range(len(table_assignments)):
    print(f"{table_assignments[i][0]} {table_assignments[i][1]}")  # Print each table assignment
