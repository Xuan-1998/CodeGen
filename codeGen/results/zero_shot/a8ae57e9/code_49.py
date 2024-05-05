# Step 1: Read the input
n = int(input())
requests = []
for _ in range(n):
    group_size, total_amount = map(int, input().split())
    requests.append((group_size, total_amount))

k = int(input())
max_table_capacity = int(input())

# Step 2: Sort the requests by the amount spent per person
requests.sort(key=lambda x: x[1] / x[0], reverse=True)

# Step 3: Initialize variables for the solution
accepted_requests = 0
total_amount_earned = 0

table_usages = [0] * k
for request in requests:
    group_size, total_amount = request
    if all(capacity >= group_size for capacity in table_usages):
        # If there's enough capacity in any table, seat the group and update the total amount earned
        table_index = table_usages.index(min(table_usages))
        table_usages[table_index] -= group_size
        accepted_requests += 1
        total_amount_earned += total_amount

# Step 4: Print the output
print(f"{accepted_requests} {total_amount_earned}")
for i in range(accepted_requests):
    request_number, table_index = requests[i]
    print(f"{request_number+1} {table_index+1}")
