import sys
input = sys.stdin.readline

def expected_carries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        sum_ = [0] * (N + 2)
        
        # Initialize dp[0][j] = 0 for all j
        for j in range(N + 1):
            sum_[j] = sum_[j - 1] if j > 0 else 0
        
        for i in range(1, N + 1):
            for j in range(i + 1):
                # If A's i-th digit is greater than or equal to (10 - j), increment sum_ by 1
                sum_[i] += 1 if int(input()) >= (10 - j) else 0
                
                # Update dp[i][j]
                for k in range(N + 1):
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i - 1][k] + (int(input()) >= (10 - k)) for k in range(N + 1))
                    
        # Return sum_[N] / ((N+1)*(N+2)/2) as the expected number of non-zero carries
        print(sum_[N] / ((N + 1) * (N + 2) // 2))

expected_carries()
