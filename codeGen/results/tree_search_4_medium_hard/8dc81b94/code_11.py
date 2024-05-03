from sys import stdin

def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n+1):
        if a[i-1] > 0:
            dp[i] = min(dp[i], dp[i-1] + a[i-1])
    
    if dp[n] == float('inf'):
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    solve()
