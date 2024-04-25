MOD = 998244353

# Read the number of sets
N = int(input())

# Initialize the dictionary for DP
dp = {}

# Read the first set and set the base case for the DP
first_set = list(map(int, input().split()))[1:]
for j in first_set:
    dp[(1, j)] = 1

# Process the remaining sets
for i in range(2, N + 1):
    current_set = list(map(int, input().split()))[1:]
    new_dp = {}
    for j in current_set:
        # Sum up the number of ways to reach the previous set without ending in j
        total_ways = sum(dp.get((i - 1, prev), 0) for prev in set(current_set) - {j}) % MOD
        new_dp[(i, j)] = total_ways
    # Update the dp dictionary
    dp = new_dp

# Calculate the final answer by summing all the ways to end the sequence with any element from the last set
answer = sum(dp.values()) % MOD

print(answer)
