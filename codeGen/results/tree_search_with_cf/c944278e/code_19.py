python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    dp = [[0] * (2 ** (n - i)) for i in range(n + 1)]
    
    # Base case: initial sequence p is just integers from 1 to 2^n
    for j in range(2 ** n):
        dp[0][j] = j + 1
    
    # Fill the dp table according to the binary string s
    for i in range(1, n + 1):
        for j in range(2 ** (n - i)):
            if s[i - 1] == '0':
                dp[i][j] = min(dp[i - 1][2 * j], dp[i - 1][2 * j + 1])
            else:
                dp[i][j] = max(dp[i - 1][2 * j], dp[i - 1][2 * j + 1])
    
    # The result is in dp[n][0]
    result = set()
    result.add(dp[n][0])
    
    # Output the sorted list of possible maximum values
    result = sorted(result)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()

