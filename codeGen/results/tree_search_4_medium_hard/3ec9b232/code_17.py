import sys

# Define a function to generate all possible partitions of n
def generate_partitions(n):
    partitions = ['0' + '1' * (n - 1)]
    for i in range(1, n):
        new_partitions = []
        for p in partitions:
            new_p = ''
            for j in range(i):
                if p[j] == '1':
                    new_p += '1' + '0' * (i - j - 1) + '0'
                else:
                    new_p += '0' + '0' * (i - j - 1)
            new_partitions.append(new_p)
        partitions = new_partitions
    return partitions

# Define a function to count the number of ways to match each partition
def count_ways_to_match(dp, i, p):
    total_ways = 0
    for j in range(i):
        if p[j] == '1':
            ways_to_match_j = dp.get(j, {}).get(p[:j], 0)
            total_ways += ways_to_match_j
    return total_ways

# Read input from stdin
n = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

# Initialize the dynamic programming dictionary
dp = {}

# Generate all possible partitions of n
partitions = generate_partitions(n)

# Count the number of ways to match each partition
for i in range(1, n + 1):
    for p in partitions:
        if i == 1:
            dp[i][p] = 1
        else:
            total_ways = count_ways_to_match(dp, i, p)
            dp[i][p] = total_ways

# Calculate the final output
output = sum(1 for v in dp[n].values() if M == sorted(list(map(int, v.split('')))))
print(output % (10**9 + 7))
