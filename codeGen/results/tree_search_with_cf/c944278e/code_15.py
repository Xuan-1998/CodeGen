python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    # Initialize dp array
    size = 2 ** n
    dp = [[0] * (size // (2 ** i)) for i in range(n + 1)]
    
    # Base case
    for j in range(size):
        dp[0][j] = j + 1
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(size // (2 ** i)):
            if s[i - 1] == '0':
                dp[i][j] = min(dp[i - 1][2 * j], dp[i - 1][2 * j + 1])
            else:
                dp[i][j] = max(dp[i - 1][2 * j], dp[i - 1][2 * j + 1])
    
    # Extract the final result
    result = sorted(set(dp[n]))
    
    # Print the result
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()

