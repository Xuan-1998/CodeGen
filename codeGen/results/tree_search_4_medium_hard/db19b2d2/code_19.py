import sys

# Read input from stdin
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Initialize the probability array
P = [[0.0 for _ in range(n + 1)] for _ in range(m)]

# Calculate the probability that there are no players from department i for k players on the team
for d in range(m):
    for k in range(n + 1):
        if d == h:
            continue
        P[d][k] = (P[d][k - 1] * s[h] / (n - k)) if k < n else 0.0

# Calculate the probability that there are at least one player from department i for k players on the team
for d in range(m):
    for k in range(n + 1):
        P[d][k] += (P[d][k - 1] * s[h] / (n - k)) if k < n else 0.0

# Calculate the final answer
answer = sum(P[h][i] for i in range(1, min(h + 1, n) + 1))

print(answer)
