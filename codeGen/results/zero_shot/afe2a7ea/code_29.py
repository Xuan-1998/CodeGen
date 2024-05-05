n = int(input())

# Calculate the total number of possible ways
total_ways = 1 << n

# Calculate the number of ways where tower is built in town 0 or n+1
bad_ways = 2 * (1 << (n - 1))

# Calculate the probability
probability = (total_ways - bad_ways) % 998244353

print(probability)
