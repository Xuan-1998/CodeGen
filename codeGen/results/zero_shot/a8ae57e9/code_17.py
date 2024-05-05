import sys

# Read input
n = int(sys.stdin.readline())
requests = []
for _ in range(n):
    ci, pi = map(int, sys.stdin.readline().split())
    requests.append((ci, pi))

k = int(sys.stdin.readline())

# Sort requests by group size
requests.sort(key=lambda x: x[0])

total_earned = 0
accepted_requests = 0

# Accept or decline requests
for ci, pi in requests:
    found_table = False
    for i in range(k):
        if ci <= ri:  # Check table capacity
            print(f"{ci} {i+1}")  # Allocate group to this table
            total_earned += pi
            accepted_requests += 1
            found_table = True
            break
    if not found_table:
        continue

print(accepted_requests, total_earned)
