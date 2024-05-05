def count_bitwise_operations(n, k):
    mod = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Initialize the base cases: one element array
    for i in range(2**k):
        and_result = i & (i - 1)
        xor_result = i ^ (i - 1)
        dp[1][and_result] += 1
        if xor_result < 2**k:
            dp[1][xor_result] += 1
    
    # Build up the solution using a bottom-up approach
    for i in range(2, n + 1):
        for j in range(k + 1):
            and_result = (j - 1) * (2 ** k - 1)
            xor_result = (j - 1) * (2 ** k - 1)
            for m in range(i):
                and_result += dp[m][j-1] * ((2**k - 1) >> j)
                xor_result += dp[m][j-1] * ((1 << k) - 1 - ((2**k - 1) >> j))
            dp[i][j] = (and_result + dp[i-1][j]) % mod
            if xor_result < 2**k:
                dp[i][j] = (dp[i][j] + (xor_result + dp[i-1][j])) % mod
    
    # Calculate the final result using bitwise AND operation on all elements
    total_and_result = 0
    for j in range(k, -1, -1):
        total_and_result = (total_and_result << 1) | ((dp[n][k] >> j) & 1)
    
    # Count arrays where the result of the bitwise AND operation is greater than or equal to the result of the bitwise XOR operation
    count = 0
    for j in range(k + 1):
        if total_and_result >= (2**j - 1):
            count += dp[n][k] % mod
    
    return count

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(count_bitwise_operations(n, k))
