import sys

def solve():
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))
    
    dp = {0: 1}
    max_val = 0
    
    for i in range(N):
        max_val = max(max_val, Arr[i])
        
        if max_val > K:
            continue
        
        new_max_val = max_val
        cumulative_sum = 0
        
        for j in range(i, N):
            new_max_val = max(new_max_val, Arr[j])
            
            if new_max_val > K:
                break
            
            cumulative_sum += 1
            dp.setdefault(cumulative_sum, 0)
            dp[cumulative_sum] += 1
    
    print(sum((cumulative_sum for cumulative_sum in dp), 0))

if __name__ == "__main__":
    solve()
