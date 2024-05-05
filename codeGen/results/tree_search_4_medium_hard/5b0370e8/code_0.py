# Define the modulo value
MOD = 10**9 + 7

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        cnt = [0] * (k+1)
        dp = [[0] * (k+1) for _ in range(n+1)]
        
        # Initialize the count dictionary
        for x in range(2**k):
            bit = 0
            while x:
                if x & 1:
                    bit += 1
                x >>= 1
            cnt[bit] += 1
        
        # Calculate dp[i][j]
        for i in range(n+1):
            for j in range(k+1):
                if i < 0 or j < 0:
                    continue
                if i == 0:
                    dp[i][j] = (dp[i][j-1] + cnt[j]) % MOD
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j] + cnt[j]) % MOD
        
        # Print the count
        print(dp[n][k])

solve()
