accepted_requests = []
total_earned = 0

for i, (group_size, total_amount) in enumerate(requests):
    accepted = False
    for j in range(k):
        table_capacity = max_capacity - sum([request[0] for request in accepted_requests if request[1] == j])
        if group_size <= table_capacity:
            accepted = True
            accepted_requests.append((i, j))
            total_earned += total_amount
            break

print(len(accepted_requests), total_earned)
for request in accepted_requests:
    print(request[0], request[1])
