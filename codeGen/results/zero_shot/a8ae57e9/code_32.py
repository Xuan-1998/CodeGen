import sys

# Read the input
n = int(sys.stdin.readline())
requests = []
for _ in range(n):
    size, amount = map(int, sys.stdin.readline().split())
    requests.append((size, amount))

k = int(sys.stdin.readline())
capacity = int(sys.stdin.readline())

# Sort the requests by amount in descending order
requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_amount_earned = 0

tables = [[capacity, 0] for _ in range(k)]
for size, amount in requests:
    for i, table in enumerate(tables):
        if table[0] >= size:
            tables[i][0] -= size
            total_amount_earned += amount
            accepted_requests += 1
            break

print(accepted_requests)
print(total_amount_earned)

# Print the accepted requests and tables
for i, (size, _) in enumerate(requests):
    if accepted_requests > i:
        for j, table in enumerate(tables):
            if table[0] >= size:
                print(i+1, j+1)
                break
