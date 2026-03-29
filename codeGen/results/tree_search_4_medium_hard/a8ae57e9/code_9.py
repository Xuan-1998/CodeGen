import sys

# Read input from stdin
n = int(sys.stdin.readline().strip())
requests = []
for _ in range(n):
    size, amount = map(int, sys.stdin.readline().split())
    requests.append((size, amount))

k, max_capacity = map(int, sys.stdin.readline().split())

# Initialize dynamic programming table
dp = [[0] * (max_capacity + 1) for _ in range(max(size for size, _ in requests) + 1)]

for i in range(1, len(requests) + 1):
    size, amount = requests[i - 1]
    for j in range(max_capacity + 1):
        if j < amount:
            dp[i][j] = dp[i - 1][j]
        else:
            accept = dp[i - 1][j - amount] + amount
            decline = dp[i - 1][j]
            dp[i][j] = max(accept, decline)

# Find the maximum amount of money earned and the corresponding number of accepted requests
max_earned = 0
accepted_requests = 0
for i in range(max_capacity + 1):
    if dp[-1][i] > max_earned:
        max_earned = dp[-1][i]
        accepted_requests = i

# Print output to stdout
print(f"{accepted_requests} {max_earned}")
