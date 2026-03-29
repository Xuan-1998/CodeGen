n, k, max_capacity = map(int, input().split())
requests = []
for _ in range(n):
    requests.append(list(map(int, input().split())))

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = []
total_earned = 0
tables = [0] * k
for request in requests:
    group_size, amount = request
    for i in range(k):
        if tables[i] + group_size <= max_capacity:
            tables[i] += group_size
            accepted_requests.append(request)
            total_earned += amount
            break

print(len(accepted_requests), total_earned)
for i, request in enumerate(accepted_requests):
    print(i+1, request[0])
