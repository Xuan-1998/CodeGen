# Read input
n = int(input())
requests = []
for _ in range(n):
    group_size, total_amount = map(int, input().split())
    requests.append((group_size, total_amount))

k = int(input())
table_capacity = int(input())

# Sort requests based on amount spent per person
requests.sort(key=lambda x: x[1] / x[0])

accepted_requests = 0
total_amount_earned = 0

for request in requests:
    group_size, total_amount = request
    if accepted_requests < k and group_size <= table_capacity:
        accepted_requests += 1
        total_amount_earned += total_amount
        print(f"{n-accept_requests} {table_capacity}")
