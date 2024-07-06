# Step 1: Read the input
n, k = map(int, input().split())  # number of booking requests and tables
requests = []
for _ in range(n):
    size, money = map(int, input().split())
    requests.append((size, money))

max_capacity, = map(int, input().split())  # maximum capacity of each table

# Step 2: Sort the requests by their total amount spent
requests.sort(key=lambda x: x[1], reverse=True)

# Step 3: Initialize variables to keep track of accepted requests and earned money
accepted_requests = 0
earned_money = 0

# Step 4: Iterate over each request, trying to seat it at a table with enough capacity
for size, money in requests:
    for i in range(k):
        if k - i > size and earned_money + money <= max_capacity:
            # Seat the group at this table
            accepted_requests += 1
            earned_money += money
            print(f"{accepted_requests} {i+1}")
            break

# Step 5: Print the final answer
print(accepted_requests, earned_money)
