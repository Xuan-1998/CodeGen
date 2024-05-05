# Step 1: Read input
n, k = map(int, input().split())
requests = []
for _ in range(n):
    group_size, total_spent = map(int, input().split())
    requests.append((group_size, total_spent))

# Step 2: Sort the booking requests by amount spent per person (total_spent / group_size)
requests.sort(key=lambda x: x[1] // x[0])

# Step 3: Initialize variables to keep track of accepted requests and tables used
accepted_requests = 0
tables_used = [0] * k

# Step 4: Iterate through the sorted booking requests
for i, (group_size, total_spent) in enumerate(requests):
    # Find a table with enough capacity for this group
    for j, table_capacity in enumerate(tables_used):
        if table_capacity + group_size <= k:
            tables_used[j] += group_size
            accepted_requests += 1
            print(f"Request {i+1} will be seated at table {j+1}")
            break

# Step 5: Print the total amount of money earned and the number of accepted requests
print(accepted_requests, sum(total_spent for _, total_spent in requests[:accepted_requests]))
