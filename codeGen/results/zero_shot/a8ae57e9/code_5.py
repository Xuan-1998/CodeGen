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
tables = [max_capacity] * k

for group_size, total_amount in requests:
    for i in range(k):
        if tables[i] >= group_size:
            tables[i] -= group_size
            accepted_requests += 1
            total_earned += total_amount
            break

print(accepted_requests)
print(total_earned)

for i in range(n):
    if i < accepted_requests:
        print(i+1, requests[i][0])
