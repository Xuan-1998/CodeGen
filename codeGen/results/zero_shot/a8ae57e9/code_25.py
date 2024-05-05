# Step 1: Read input
n = int(input())  # number of booking requests
requests = []
for _ in range(n):
    size, money = map(int, input().split())
    requests.append((size, money))

k = int(input())  # number of tables
capacity = int(input())  # maximum capacity of each table

# Step 2: Sort requests by group size and then by total amount of money spent
requests.sort(key=lambda x: (x[0], -x[1]))

# Step 3: Initialize variables to keep track of accepted requests, total money earned, and assigned tables
accepted_requests = 0
total_money_earned = 0
table_assignments = []

# Step 4: Iterate over requests and assign them to tables if possible
for size, money in requests:
    for i in range(k):
        if table_assignments and table_assignments[-1][1] + size <= capacity:
            break
    else:
        continue

    accepted_requests += 1
    total_money_earned += money
    table_assignments.append((accepted_requests, i))

# Step 5: Print output
print(accepted_requests, total_money_earned)
for request, table in table_assignments:
    print(request, table)
