def count_ones(n):
    dp = [0] * (n + 1)
    
    # Base case: no ones at positions 0-9 (0-9 are single-digit numbers)
    for i in range(10):
        dp[i] = 1
    
    # Calculate the total count of ones for each digit position
    for i in range(10, n + 1):
        dp[i] = dp[i - 1] + i // (10 ** ((i.bit_length() - 1) // 4))
    
    return sum(dp)

# Example usage:
n = int(input())
print(count_ones(n))
