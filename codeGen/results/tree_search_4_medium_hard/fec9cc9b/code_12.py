import sys

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n):
        if arr[i] >= arr[i - 1]:
            dp[i] = dp[i - 1]
        else:
            prev_non_decreasing_idx = max(j for j in range(i) if arr[j] <= arr[i])
            dp[i] = dp[prev_non_decreasing_idx]
    
    for _ in range(m):
        l, r = map(int, input().split())
        
        is_ladder = True
        for i in range(l - 1, r):
            if arr[i] > arr[i + 1]:
                is_ladder = False
                break
        
        print("Yes" if is_ladder else "No")

if __name__ == "__main__":
    main()
