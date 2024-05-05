import sys

def prob_set_signal_powers(n):
    # Calculate the number of ways to place radio towers
    tower_ways = 1 << n  # 2^n possible combinations
    
    # Initialize probability variables
    ans = 0
    mod = 998244353
    
    for i in range(tower_ways):
        # Check if current combination is valid
        valid = True
        for j in range(n):
            if (i >> j) & 1:  # If tower is at this position
                for k in range(j+1, n+1):  # Check other towns
                    if (k != 0 and i >> k-1) & 1:  # If tower is also here
                        valid = False
                        break
        
        if valid:
            ans += 1
    
    return ans % mod

# Read input from stdin
n = int(sys.stdin.readline())

# Calculate the probability
ans = prob_set_signal_powers(n)

# Print the answer to stdout
print(ans)
