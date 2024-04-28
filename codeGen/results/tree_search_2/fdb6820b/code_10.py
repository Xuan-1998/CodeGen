import sys

def solve():
    m, N = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Initialize the dp table with 0s
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for num in arr:
        for i in range(N, num - 1, -1):
            dp[i] += dp[i - num]
    
    # Calculate the total number of ways to form N
    total_ways = dp[N] % (10**9 + 7)
    
    print(total_ways)

if __name__ == "__main__":
    solve()
