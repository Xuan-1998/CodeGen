python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    
    # Initialize dp table
    size = 2 ** n
    dp = [[0] * size for _ in range(n + 1)]
    
    # Base state
    for j in range(size):
        dp[0][j] = j + 1
    
    # Fill dp table
    for i in range(1, n + 1):
        step = 2 ** (n - i)
        for j in range(0, size, step * 2):
            for k in range(step):
                if s[i - 1] == '0':
                    dp[i][j + k] = min(dp[i - 1][j + k], dp[i - 1][j + k + step])
                else:
                    dp[i][j + k] = max(dp[i - 1][j + k], dp[i - 1][j + k + step])
    
    # Collect unique values from dp[n][0:step]
    result_set = set(dp[n][j] for j in range(step))
    result = sorted(result_set)
    
    # Print the result
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()

