def solve(n, a):
    # Step 2: Define the DP states
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Step 3: Handle base cases
    for i in range(n + 1):
        dp[i][i] = 1
    
    # Step 4: Update the DP states recursively
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if a[j] % (length) == 0:
                dp[i][j] = (dp[i][i + length - 1] + dp[i + 1][j]) % (10**9 + 7)
    
    # Step 5: Return the answer
    return dp[0][n-1]

def main():
    n, a = process_input()
    print(solve(n, a))

if __name__ == "__main__":
    main()

