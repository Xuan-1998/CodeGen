import sys
from collections import defaultdict

T = int(input())  # number of test cases

for _ in range(T):
    N = int(input())  # maximum number of digits in A and B
    
    dp = [[[0.0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    
    for k in range(1, N+1):
        for i in range(N-k+1):
            for j in range(N-k+1):
                if k == 1:
                    dp[i][j][k] = (i+j)/10.0
                else:
                    dp[i][j][k] = sum((dp[i-1][j-1][min(k, m)] + i+j) / 10.0 for m in range(min(k, N-k+1)+1)) / (2**(N-k))
    
    total_carries = sum(dp[N//2][N//2][k] for k in range(N//2+1))
    expected_carries = total_carries / (2**N)
    
    print(expected_carries)
