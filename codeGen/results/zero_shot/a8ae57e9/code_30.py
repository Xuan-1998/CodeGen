# Step 1: Read input
n, k, max_capacity = map(int, input().split())
requests = []
for _ in range(n):
    group_size, money = map(int, input().split())
    requests.append((group_size, money))

# Step 2: Sort requests by total amount of money descending
requests.sort(key=lambda x: x[1], reverse=True)

# Step 3: Initialize accepted requests and tables used
accepted_requests = 0
used_tables = [False] * k

# Step 4: Iterate over requests to find the best ones
for group_size, money in requests:
    # Check if there's enough capacity for the group
    if any(not used_tables[i] and i >= group_size - 1 for i in range(k)):
        # Find a table with enough capacity for the group
        for i in range(k):
            if not used_tables[i] and i >= group_size - 1:
                used_tables[i] = True
                break
        
        # Increment accepted requests and total money earned
        accepted_requests += 1

# Step 5: Print output
print(accepted_requests, sum(request[1] for request in requests[:accepted_requests]))
for i in range(accepted_requests):
    print(i+1, requests[i][0]-1)
