import sys

# Read input
n = int(sys.stdin.readline())
requests = []
for _ in range(n):
    ci, pi = map(int, sys.stdin.readline().split())
    requests.append((ci, pi))

k = int(sys.stdin.readline())

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_money_earned = 0

tables = [0] * k

for ci, pi in requests:
    while True:
        for i, table in enumerate(tables):
            if table + ci <= k:
                tables[i] += ci
                total_money_earned += pi
                accepted_requests += 1
                break
        else:
            continue
        break

# Print output
print(accepted_requests, total_money_earned)

for i, (ci, _) in enumerate(requests):
    for j, table in enumerate(tables):
        if table >= ci:
            print(i + 1, j + 1)
            tables[j] -= ci
            break
