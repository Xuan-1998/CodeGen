def calculate_expected_carry(N):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: there are no carries when adding a single digit.
    for i in range(N + 1):
        dp[i][0] = dp[0][i] = 0
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # Calculate the expected number of non-zero carries using the recursive formula.
            if i < N:
                dp[i][j] = sum((dp[k-1][l-1] for k in range(i+1, N+1) for l in range(j+1, N+1))) / ((N-i)*(N-j))
            else:
                dp[i][j] = 0
    
    # Return the value of dp[0][0] as the expected number of non-zero carries when adding A and B.
    return dp[0][0]

# Read input from stdin.
T = int(input())

for _ in range(T):
    N = int(input())
    
    # Calculate and print the expected number of non-zero carries for each test case.
    print(calculate_expected_carry(N))
