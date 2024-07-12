python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    # Initial sequence from 1 to 2^n
    initial_sequence = list(range(1, 2**n + 1))
    
    # dp table where dp[i][mask] is a set of possible maximum values
    dp = [set() for _ in range(n + 1)]
    
    # Base case: dp[0] is the initial sequence
    dp[0] = set(initial_sequence)
    
    # Process each bit in the string s
    for i in range(n):
        next_dp = set()
        # Compare pairs according to the current bit
        if s[i] == '0':
            # Keep the minimum of each pair
            for j in range(0, len(initial_sequence), 2):
                next_dp.add(min(initial_sequence[j], initial_sequence[j + 1]))
        else:
            # Keep the maximum of each pair
            for j in range(0, len(initial_sequence), 2):
                next_dp.add(max(initial_sequence[j], initial_sequence[j + 1]))
        
        # Update the dp table
        dp[i + 1] = next_dp
        # Update initial_sequence for the next iteration
        initial_sequence = sorted(next_dp)
    
    # The result is the possible maximum values after processing all bits
    result = sorted(dp[n])
    
    # Print the result
    print(" ".join(map(str, result)))


