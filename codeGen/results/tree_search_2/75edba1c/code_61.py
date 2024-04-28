import sys

def solve():
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))
    
    dp = [0] * (N + 1)
    max_val = 0
    
    for i in range(N):
        max_val = max(max_val, Arr[i])
        
        if max_val > K:
            dp[i+1] = dp[i] + 1
        else:
            dp[i+1] = dp[i]
    
    print(dp[N-1])

if __name__ == "__main__":
    solve()
