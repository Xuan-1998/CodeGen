import sys

n = int(sys.stdin.readline())
requests = [tuple(map(int, line.split())) for line in sys.stdin.readlines()[:n]]
k, max_capacity = map(int, sys.stdin.readline().split())

accepted_requests = 0
total_earnings = 0

requests.sort(key=lambda x: x[1], reverse=True)

for i, (group_size, amount) in enumerate(requests):
    if group_size <= k * max_capacity:
        accepted_requests += 1
        total_earnings += amount
        table_number = min(i // (k - 1), k - 1) + 1
        print(f"{i} {table_number}")

print(f"{accepted_requests} {total_earnings}")
