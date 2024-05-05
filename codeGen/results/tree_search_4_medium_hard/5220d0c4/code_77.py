def max_beauty(nums, bad_primes):
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    # Initialize dp[0][n-1] to the beauty value of the entire array
    for i in range(n):
        dp[i][n - 1] = nums[i]

    # Fill the table row by row, from left to right
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            last_num = nums[end]
            is_good_prime = not any(last_num % prime == 0 for prime in bad_primes)
            if is_good_prime:
                dp[start][end] = min(dp[start][end], dp[start][end - 1] + (next_prime(last_num) - 1))
            else:
                dp[start][end] = dp[start][end - 1]

    # Return the maximum beauty value in the bottom-right cell
    return max(dp[0])

def next_prime(n):
    if n <= 2:
        return 2
    prime = 3
    while True:
        if n % prime == 0:
            break
        prime += 2
    return prime

import sys
input = sys.stdin.read().split()
n, m = map(int, input[:2])
nums = list(map(int, input[2:]))
bad_primes = list(map(int, input[3:]))

print(max_beauty(nums, bad_primes))
