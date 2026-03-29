def count_blocks(n):
    MOD = 998244353
    dp = [[0] * 10 for _ in range(11)]
    
    # base case: There is only one way to form a block with 1 consecutive equal digit (the digit itself)
    dp[1] = [10 ** (n - 1)] * 10
    
    for k in range(2, n + 1):
        for d in range(10):
            # If the first k-1 digits are not equal to each other
            if k > 1:
                dp[k][d] += sum(dp[k - 1][:]) * 10 ** (n - k)
            
            # If the first k-1 digits are equal to each other
            if d == 0 or d == 9:  # special case for 0 and 9
                dp[k][d] += dp[k - 2][0] * 10 ** (n - k + 1)
            else:
                dp[k][d] += sum(dp[k - 1][1:]) * 10 ** (n - k)  # all other cases
            
            # modulo operation to avoid overflow
            dp[k][d] %= MOD
    
    return [str(int(x)) for x in dp[n]]

if __name__ == "__main__":
    n = int(input())
    print(*count_blocks(n), sep=' ')
