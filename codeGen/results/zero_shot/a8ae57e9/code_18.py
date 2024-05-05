import sys

n = int(sys.stdin.readline())
requests = []
for _ in range(n):
    group_size, total_spent = map(int, sys.stdin.readline().split())
    requests.append((group_size, total_spent))

requests.sort(key=lambda x: x[1], reverse=True)

k = int(sys.stdin.readline())
table_capacity = int(sys.stdin.readline())

accepted_requests = 0
total_earned = 0
table_usage = [0] * k

assignments = {}

for group_size, total_spent in requests:
    for i in range(k):
        if table_usage[i] + group_size <= table_capacity:
            accepted_requests += 1
            total_earned += total_spent
            assignments[accepted_requests] = (group_size, i)
            table_usage[i] += group_size
            break

print(accepted_requests, total_earned)

for request_num in range(1, accepted_requests + 1):
    print(f"{request_num} {assignments[request_num][1]}")
