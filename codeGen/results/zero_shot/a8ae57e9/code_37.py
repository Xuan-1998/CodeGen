accepted_requests = 0
total_amount_earned = 0
table_capacities = [max_capacity] * k

for request in requests:
    group_size, total_amount = request
    for i, capacity in enumerate(table_capacities):
        if capacity >= group_size:
            table_capacities[i] -= group_size
            accepted_requests += 1
            total_amount_earned += total_amount
            break

output = [accepted_requests, total_amount_earned]
for i in range(accepted_requests):
    output.append([i + 1, table_capacities.index(max(table_capacities)) + 1])

print(*output)
