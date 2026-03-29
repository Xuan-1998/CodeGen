# Step 1: Read input
n, k = map(int, input().split())
requests = []
for _ in range(n):
    group_size, total_amount = map(int, input().split())
    requests.append((group_size, total_amount))

# Step 2: Sort requests based on amount spent per person (amount / group size)
requests.sort(key=lambda x: x[1] // x[0], reverse=True)

# Step 3: Initialize variables
accepted_requests = 0
total_earned = 0

# Step 4: Iterate over the sorted requests and seat each group
for request in requests:
    group_size, total_amount = request
    for i in range(k):  # Try to seat this group at each table
        if i < group_size:  # If the group can fit in this table
            accepted_requests += 1
            total_earned += total_amount
            print(f"{accepted_requests} {i+1}")
            break

print(accepted_requests, total_earned)
