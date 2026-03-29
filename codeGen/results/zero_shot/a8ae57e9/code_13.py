import sys

n = int(sys.stdin.readline())
requests = []
for _ in range(n):
    size, amount = map(int, sys.stdin.readline().split())
    requests.append((size, amount))

k = int(sys.stdin.readline())
max_capacity = int(sys.stdin.readline())

accepted_requests = 0
total_earnings = 0

requests.sort(key=lambda x: x[1], reverse=True)

for size, amount in requests:
    if accepted_requests < k and size <= max_capacity:
        accepted_requests += 1
        total_earnings += amount

print(accepted_requests)
print(total_earnings)

table_numbers = []
for i in range(k):
    table_numbers.append(f"Table {i+1}")

print("\n".join([f"{i+1} {j}" for i, (size, _) in enumerate(requests) for j, _ in enumerate(table_numbers)]))
