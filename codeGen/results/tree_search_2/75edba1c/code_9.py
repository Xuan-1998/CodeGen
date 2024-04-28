import sys

def solve():
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))
    
    dp = [0] * (N + 1)
    max_val = 0
    
    for i in range(N - 1, -1, -1):
        max_val = max(max_val, Arr[i])
        
        if max_val > K:
            dp[i] = 1
        else:
            if i < N and max(Arr[i:i+2]) > K:
                dp[i] = 1
        
    print(sum(dp))

if __name__ == "__main__":
    solve()
