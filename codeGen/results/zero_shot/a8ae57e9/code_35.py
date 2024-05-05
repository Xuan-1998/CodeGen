import heapq

requests.sort(key=lambda x: requests[x][1], reverse=True)
accepted_requests = 0
total_amount_earned = 0
table_usage = [0] * k
for request_id in requests:
    group_size, amount = requests[request_id]
    for i in range(k):
        if table_usage[i] + group_size <= capacity:
            table_usage[i] += group_size
            accepted_requests += 1
            total_amount_earned += amount
            break

print(accepted_requests)
print(total_amount_earned)
for request_id in sorted(requests.keys()):
    if requests[request_id][0] > 0:
        print(request_id, min(range(k), key=lambda x: table_usage[x]))
