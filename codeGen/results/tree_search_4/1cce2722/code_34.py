import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = max(dp[i-1], 
                    sum((k-i) + (n-k) - (a[i] - a[k]) for k in range(min(i, n)) if abs(a[i] - a[k]) <= 2))
    
    print(max(dp))

if __name__ == "__main__":
    solve()
