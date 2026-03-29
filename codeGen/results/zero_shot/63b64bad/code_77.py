# Read input
n = int(input())
sequence = list(map(int, input().split()))

# Initialize result array
result = [0] * (n - 1)

# Iterate over each sequence
for i in range(2, n + 1):
    x, y = 1, 0
    while x > 0 and x <= n:
        x += sequence[i - 1]
        y += sequence[i - 1]
        x -= sequence[i - 1]
    result[i - 2] = y if x > 0 else -1

# Print output
for i, val in enumerate(result):
    print(val)
