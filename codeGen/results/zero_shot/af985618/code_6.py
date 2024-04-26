MOD = 998244353

def add_mod(a, b, mod):
    return (a + b) % mod

def mul_mod(a, b, mod):
    return (a * b) % mod

def main():
    n = int(input())
    A = [input().split() for _ in range(n)]
    
    # Initialize the dynamic programming table
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        if A[i - 1][0] == '+':
            x = int(A[i - 1][1])
            for j in range(i + 1):
                # If we don't include the current positive element
                dp[i][j] = add_mod(dp[i][j], dp[i - 1][j], MOD)
                # If we include the current positive element
                if j > 0:
                    dp[i][j] = add_mod(dp[i][j], mul_mod(dp[i - 1][j - 1], x, MOD), MOD)
        else:
            for j in range(i):
                # If we don't include the current negative element
                dp[i][j] = add_mod(dp[i][j], dp[i - 1][j], MOD)
                # If we include the current negative element (effect of removing the smallest element)
                dp[i][j] = add_mod(dp[i][j], dp[i - 1][j + 1], MOD)
    
    # Calculate the sum of f(B) for all subsequences B
    result = 0
    for j in range(1, n + 1):
        result = add_mod(result, dp[n][j], MOD)
    
    print(result)

if __name__ == "__main__":
    main()
