import sys

def solve():
    t = int(input())
    mod = 10**9 + 7
    
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[False] * (2**(k-1)) for _ in range(n+1)]
        
        # Base case: All bits are unset
        dp[0][0] = True
        
        for i in range(1, n+1):
            for j in range(2**(k-1)):
                # If the current element's value is less than or equal to the mask,
                # then it can only be 0 in all elements.
                if (j & ((1 << k) - 1)) >= i:
                    dp[i][j] = any(dp[i-1][m] for m in range(2**(k-1)) if (j & m) == j)
                else:
                    # If the current element's value is greater than the mask,
                    # then it must be 1 in at least one element.
                    dp[i][j] = any(dp[i-1][m] for m in range(2**(k-1)) if (j & m) == j) or not all((j & (1 << bit)) for bit in range(k-1, -1, -1))
        
        # Count the number of arrays for which the result of the bitwise AND operation is 
        # greater than or equal to the result of the bitwise XOR operation on all elements.
        ans = sum(1 for j in range(2**(k-1)) if dp[n][j])
        print(ans % mod)

if __name__ == "__main__":
    solve()
