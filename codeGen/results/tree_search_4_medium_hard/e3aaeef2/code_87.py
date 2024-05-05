import sys
MOD = int(1e9) + 7
MAX_N = int(1e9)

# Precompute values for each digit from 0 to 9 and store them in an array
dp_digits = [i+1 for i in range(10)]

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        # Initialize dp table with zeros
        dp = [[0] * (m + 1) for _ in range(MAX_N + 1)]
        
        # Base cases: no more operations or one operation left
        for i in range(1, MAX_N + 1):
            if m == 0:
                dp[i][0] = 0
            elif m == 1:
                dp[i][1] = 1 if i % 10 != 0 else 2
        
        # Fill up the dp table using dynamic programming
        for i in range(1, MAX_N + 1):
            for j in range(m + 1):
                if j % 2 == 0:
                    dp[i][j] = 1 + dp[i//10**(dp_digits[int(i/10**9)%10]-1)][j-1]
                else:
                    if i % 10 != 0:
                        dp[i][j] = 1 + dp[i//10**(dp_digits[int(i/10**9)%10]-1)][j-1]
                    else:
                        dp[i][j] = 2
        
        # Print the length of the resulting number after m operations, modulo MOD
        print(dp[n][m] % MOD)

if __name__ == "__main__":
    solve()
