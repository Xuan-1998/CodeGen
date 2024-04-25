MOD = 998244353

def solve(N, sets):
    # Initialize dp table
    dp = [{} for _ in range(N)]
    
    # Base case: for the first set, all elements can be the last element
    for x in sets[0]:
        dp[0][x] = 1
    
    # Fill dp table
    for i in range(1, N):
        for x in sets[i]:
            # Case 1: x was not the last element in the previous set
            dp[i][x] = sum(dp[i-1].values()) % MOD
            # Case 2: x was the last element in the previous set
            if x in dp[i-1]:
                dp[i][x] = (dp[i][x] - dp[i-1][x] + MOD) % MOD
    
    # The answer is the sum of all possible last elements in the last set
    return sum(dp[-1].values()) % MOD

# Read input
N = int(input())
sets = []
for _ in range(N):
    line = list(map(int, input().split()))
    sets.append(line[1:])  # Ignore the size of the set

# Compute and print the answer
print(solve(N, sets))
