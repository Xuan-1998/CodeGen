import sys

def calculate_mex(pairs):
    # The MEX is the smallest non-negative integer not present in the pairs set
    for mex in range(4):
        if mex not in pairs:
            return mex
    return 4  # All pairs are present, so MEX is 4

def solve(n, top, bottom):
    dp = [0] * (n + 1)
    current_pairs = set()
    
    for i in range(1, n + 1):
        pair = (int(top[i - 1]), int(bottom[i - 1]))
        if pair in current_pairs:
            # Continue the current partition
            dp[i] = dp[i - 1]
        else:
            # Calculate the MEX for the current partition and consider starting a new one
            current_mex = calculate_mex(current_pairs)
            dp[i] = dp[i - 1] + current_mex
            current_pairs = {pair}
    
    # Add MEX for the last partition
    dp[n] += calculate_mex(current_pairs)
    return dp[n]

# Read the number of test cases
t = int(sys.stdin.readline().strip())

# Process each test case
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    top = sys.stdin.readline().strip()
    bottom = sys.stdin.readline().strip()
    result = solve(n, top, bottom)
    print(result)
