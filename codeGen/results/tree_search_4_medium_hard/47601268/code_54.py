def solve(n):
    dp = {}
    for i in range(0, n+1):
        bin_i = bin(i)[2:]
        dp[i] = False  # Initialize DP state to False
        prev_one = -1  # Keep track of the previous one (if any)
        for j in range(len(bin_i)):
            if bin_i[j] == '1':
                if prev_one != j-1:  # Consecutive ones don't exist
                    dp[i] = True
                    break
                prev_one = j
        if not dp[i]:  # If no consecutive ones, increment the count
            nontoggle_count += 1
    return nontoggle_count
