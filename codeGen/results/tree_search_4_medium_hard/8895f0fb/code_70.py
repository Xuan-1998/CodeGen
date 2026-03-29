import sys

def expectedCarries(N):
    dp = [[0.0 for _ in range(N+1)] for _ in range(N+1)]
    
    for i in range(N+1):
        for k in range(1, min(i+1, N+1)):
            if k == 1:
                dp[i][k] = 0
            else:
                carrySum = 0.0
                for j in range(min(k,10)): # considering digits from 0 to 9
                    numCarries = sum(1 for _ in range(max(i-j,k-1-j)))
                    carrySum += numCarries / (10**j)
                dp[i][k] = carrySum + dp[i-k][k-1]
    
    return sum([sum(dp[i]) for i in range(N+1)]) / ((N+1)*(N+2)/2)

T = int(input())
for _ in range(T):
    N = int(input())
    print(expectedCarries(N))
