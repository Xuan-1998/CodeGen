import sys

def solve():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    
    dp = {0: True}
    for i in range(n):
        total_sum = sum(arr[:i+1])
        if total_sum not in dp:
            dp[total_sum] = False
        else:
            dp[total_sum] = not dp[total_sum]
        
        total_sum = sum(arr[i:])
        if total_sum not in dp:
            dp[total_sum] = False
        else:
            dp[total_sum] = not dp[total_sum]
    
    print("YES" if dp.get(0, False) else "NO")

solve()
