n = int(input())
requests = []
for _ in range(n):
    group_size, total_amount = map(int, input().split())
    requests.append((group_size, total_amount))
requests.sort(key=lambda x: x[1], reverse=True)

k = int(input())
max_capacity = int(input())

tables = [max_capacity] * k
accepted_requests = 0
total_amount_earned = 0

for group_size, total_amount in requests:
    for i, capacity in enumerate(tables):
        if capacity >= group_size:
            tables[i] -= group_size
            accepted_requests += 1
            total_amount_earned += total_amount
            print(f"Accepted request {accepted_requests} to table {i+1}")
            break

print(accepted_requests)
print(total_amount_earned)

for i in range(accepted_requests):
    print(f"Request {i+1} to table {tables.index(max(tables))+1}")
