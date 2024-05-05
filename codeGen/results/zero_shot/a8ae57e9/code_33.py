# Step 1: Read input
n, k, ci = map(int, input().split())
requests = [list(map(int, input().split())) for _ in range(n)]

# Step 2: Sort requests by total amount of money they will spend
requests.sort(key=lambda x: x[1], reverse=True)

# Step 3: Initialize variables to keep track of accepted requests and tables used
accepted_requests = 0
tables_used = [0] * k

# Step 4: Iterate over the sorted requests
for request in requests:
    group_size, total_amount = request
    # Check if there's a table with enough capacity for this group
    for i, table_capacity in enumerate(tables_used):
        if table_capacity + group_size <= ci:
            tables_used[i] += group_size
            accepted_requests += 1
            print(f"{accepted_requests} {i+1}")
            break

# Step 5: Calculate the total amount of money earned from these requests
total_earned = sum(request[1] for request in requests[:accepted_requests])

print(f"{accepted_requests} {total_earned}")
