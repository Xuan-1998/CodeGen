import sys

def solve():
    n = int(input())
    s = input().strip()
    
    # Create a 1D prefix sum array for the binary string s
    ps = [0]
    or_val = 0
    for i in range(n):
        or_val = (or_val << 1) | int(s[i])
        ps.append(or_val)
    
    # Initialize the memoization dictionary
    dp = {}
    
    # Update the memoization table by considering all possible pairs of non-empty substrings
    for j in range(2, n+1):
        for i in range(j-1):
            # Calculate max(or(dp[i][j-1], dp[j-1][n]), or(dp[i][j], dp[n][j]))
            dp[(i, j)] = max(ps[j] - ps[i], dp.get((i+1, j-1), 0) | dp.get((j-1, n), 0))
    
    # Find the maximum bitwise OR value for any given pair of non-empty substrings
    ans = 0
    for i in range(n):
        for j in range(i+1, n+1):
            ans = max(ans, dp[(i, j)])
    
    print(bin(ans)[2:].zfill(n).lstrip('0') or '0')

if __name__ == "__main__":
    solve()
