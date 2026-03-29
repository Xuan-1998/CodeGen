def count_blocks(n):
    dp = [[0]*10 for _ in range(11)]
    
    # Initialize base case: Count blocks ending at each digit position for length 1
    for i in range(10):
        dp[i][0] = 1
    
    # Fill up memoization array using dynamic programming
    for len_ in range(1, n+1):
        for digit in range(10):
            total = 0
            for prev_digit in range(10):
                if (digit == prev_digit or prev_digit == 0) and prev_digit != digit:
                    total += dp[prev_digit][len_-1]
            dp[digit][len_] = (total + 998244353) % 998244353
    
    # Print the count of blocks of each length
    for len_ in range(1, n+1):
        print(dp[0][len_], end=' ')
