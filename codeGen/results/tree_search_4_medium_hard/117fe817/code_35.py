def count_ones(n):
    dp = {}
    
    # Initialize base case
    for i in range(10):
        if i < 1:
            continue
        dp[0][i] = i == 1
    
    # Fill up the dynamic programming table
    num_digits_n = len(str(n))
    for k in range(1, num_digits_n + 1):
        for m in range(10**k):
            if m < 10**(k-1) and k > 1:
                dp[k][m] = dp[k-1][int(str(m)[0])] + (m % 10 == 1)
            else:
                dp[k][m] = m % 10 == 1
    
    return sum(dp[num_digits_n].values())

if __name__ == "__main__":
    n = int(input())
    print(count_ones(n))
