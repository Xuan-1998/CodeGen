n = int(input())
requests = []
for _ in range(n):
    group_size, total_amount = map(int, input().split())
    requests.append((group_size, total_amount))

k = int(input())
max_capacity = int(input())

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_earned = 0
for i, (group_size, total_amount) in enumerate(requests):
    if accepted_requests >= k:
        break
    
    for j in range(k):
        if group_size <= max_capacity and sum(x[0] for x in requests[:i]) + group_size <= k * max_capacity:
            print(i+1, j+1)
            accepted_requests += 1
            total_earned += total_amount
            break

print(accepted_requests, total_earned)
