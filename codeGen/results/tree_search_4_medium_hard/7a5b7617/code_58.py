from collections import defaultdict

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    # Handle edge case: if N or M is 1
    if N == 1:
        print(1)
    elif M == 1:
        print(N)
    else:
        
        dp = defaultdict(int)
        for i in range(M+1):
            dp[i] = 1
        
        for i in range(2, N+1):
            new_dp = defaultdict(int)
            for j in range(i*M, -1, -1):
                sum_val = j
                for k in range(i-1, -1, -1):
                    if sum_val <= M:
                        new_dp[sum_val] += dp[k]
                    sum_val -= k
            dp = new_dp
        
        # Calculate the answer
        MOD = 10**9 + 7
        res = 0
        for i in range(M+1):
            res = (res + dp[i]) % MOD
        
        print(res)
