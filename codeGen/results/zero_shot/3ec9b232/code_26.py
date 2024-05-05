import sys

def solve():
    n = int(sys.stdin.readline())
    m = list(map(int, sys.stdin.readline().split()))
    
    # Initialize a table to store the number of ways to create V
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(n):
        for j in range(i + 1):
            if m[i] == j:
                dp[i + 1] += dp[j]
    
    print(dp[n] % (10**9 + 7))

if __name__ == "__main__":
    solve()
