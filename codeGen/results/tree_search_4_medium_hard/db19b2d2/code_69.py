import sys

# Read input from stdin
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Initialize variables for dynamic programming
dp_interest = False
dp_total = 0

for i in range(m):
    si = s[i]
    if si >= n:
        dp_interest = True
        dp_total += 1
    elif si < n and i == h - 1:  # edge case: last department, not enough players
        print(-1)
        sys.exit(0)

# Calculate probability
prob = dp_interest / (2 ** m)  # 2^m is the total number of possible teams

print("{:.6f}".format(prob))
