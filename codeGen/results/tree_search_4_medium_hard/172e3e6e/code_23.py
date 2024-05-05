import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = {0: 1}
    for i in range(1, n):
        dp[i] = sum((a[i]%j==0)*len(range(j+1, i+1))*dp[j] for j in range(i) if j in dp)
    
    print(dp[n-1])

if __name__ == "__main__":
    solve()
