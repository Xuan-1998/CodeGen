// Initialize dp table
dp = [[0] * (m + 1) for _ in range(n + 1)]

// Fill first row of dp table
for i in range(1, n + 1):
    is_good_prime = is_prime(arr[i - 1]) and arr[i - 1] % 2 == 0
    bad_prime_value = min_prime_divisor(arr[i - 1])
    good_prime_value = min_prime_divisor(arr[i - 1]) if is_good_prime else 0
    dp[i][0] = max(dp[i - 1][0], good_prime_value, bad_prime_value)

// Fill rest of dp table
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if is_good_prime:
            # Update cell with maximum beauty value considering last element as a good prime
            dp[i][j] = max(dp[i - 1][j], min_prime_divisor(arr[i - 1]), dp[i - 1][j - 1])
        else:
            # Update cell with maximum beauty value considering last element as a bad prime
            dp[i][j] = max(dp[i - 1][j], min_prime_divisor(arr[i - 1]), dp[i - 1][j - 1])

# The maximum beauty value of the entire array is stored in the bottom-right cell of the table
print(max(dp[n][m], key=lambda x: x))
