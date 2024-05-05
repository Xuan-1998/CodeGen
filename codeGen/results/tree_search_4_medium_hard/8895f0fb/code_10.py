import sys

# read T, the number of test cases
T = int(sys.stdin.readline())

for _ in range(T):
    # read N, the maximum number of digits in A and B
    N = int(sys.stdin.readline())
    
    # initialize a 2D DP table to store the number of non-zero carries for each pair of digits
    dp = [[[0] * (10,) for _ in range(10)] for _ in range(N)]
    
    # base case: when either i or j is equal to N-1, there would be no carry since we can only add single-digit numbers together
    for i in range(N):
        for j in range(10):
            dp[i][j][0] = 0
    
    for i in range(N - 1):
        for j in range(10):
            # transition rule: consider all possible carries when adding ai and bj
            for k in range(j + 1, 10):
                if (i > 0 and dp[i - 1][j][k] > 0) or (j > 0 and dp[i][j - 1][k] > 0):
                    dp[i][j][k] = 1
    
    # calculate the expected number of non-zero carries
    total_carries = 0
    for i in range(N):
        for j in range(10):
            total_carries += sum(dp[i][j])
    
    expected_carries = total_carries / (10 ** N) * (N - 1)
    
    print(expected_carries)
