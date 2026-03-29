import sys

k = int(input())
capacity = int(input())

requests = []
for _ in range(int(input())):
    group_size, amount = map(int, input().split())
    requests.append((group_size, amount))

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_earned = 0

for i, (group_size, amount) in enumerate(requests):
    for j in range(k):
        if j * capacity >= group_size:
            accepted_requests += 1
            total_earned += amount
            print(f"Accepted request {i+1} and seated them at table {j+1}")
            break

print(accepted_requests, total_earned)
