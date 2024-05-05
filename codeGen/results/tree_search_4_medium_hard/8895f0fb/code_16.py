import sys

def solve(N):
    dp = [[0 for _ in range(10)] for _ in range(N+1)]
    
    # Fill up the DP table
    for i in range(N+1):
        for j in range(10):
            if i == 0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = sum(dp[k][9] for k in range(i))
            else:
                carry_sum = 0
                for k in range(min(i, 9)):
                    if int(str(9-k) + str(j-1)) >= 10:
                        carry_sum += 1
                dp[i][j] = dp[i-1][j-1] + carry_sum
    
    # Calculate the expected number of non-zero carries
    total_carry = sum(dp[N][i] for i in range(10))
    expected_carry = total_carry / (10**N)
    
    return float(expected_carry)

T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))
