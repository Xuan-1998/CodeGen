# Read the input
n = int(input())
M = list(map(int, input().split()))

# Initialize an array to store the number of ways for each value
ways = [0] * (n + 1)

# For each value in M, find the number of ways to create V that results in this value
for m in M:
    for i in range(m, 0, -1):
        ways[i] += ways[i-1]

# Print the answer modulo 10^9+7
print(ways[n] % (10**9 + 7))
