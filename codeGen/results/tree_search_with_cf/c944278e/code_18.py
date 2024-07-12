python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    # Initialize dp table
    dp = [[0] * (2**(n - i)) for i in range(n + 1)]
    
    # Base case: dp[0][j] = j + 1 for all j in the range [0, 2^n - 1]
    for j in range(2**n):
        dp[0][j] = j + 1
    
    # Fill dp table according to the transition rules
    for i in range(n):
        for j in range(2**(n - i - 1)):
            if s[i] == '0':
                dp[i + 1][j] = min(dp[i][2 * j], dp[i][2 * j + 1])
            else:
                dp[i + 1][j] = max(dp[i][2 * j], dp[i][2 * j + 1])
    
    # Collect the possible maximum values
    possible_max_values = set(dp[n][0:1])
    
    # Convert to sorted list
    result = sorted(possible_max_values)
    
    # Print the result
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()

