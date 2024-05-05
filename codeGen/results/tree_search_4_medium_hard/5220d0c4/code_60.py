def max_beauty(array, bad_primes):
    n = len(array)
    dp = [[0, 0] for _ in range(n)]

    # Initialize the base case where i is 0
    dp[0][n-1][0] = array[0]
    dp[0][n-1][1] = array[0]

    for i in range(1, n):
        for j in range(i, n):
            if array[i] % 2 == 0:
                # If the current number is even, we can either keep it as is or change it to its minimum prime divisor
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])
                if array[i] in bad_primes:
                    dp[i][j][1] = 0
                else:
                    # Find the minimum prime divisor of the current number
                    min_prime_divisor = find_min_prime_divisor(array[i])
                    dp[i][j][1] = max(dp[i-1][j][0], dp[i-1][j][1]) - min_prime_divisor
            else:
                # If the current number is odd, we can either keep it as is or change it to its minimum prime divisor
                if array[i] in bad_primes:
                    dp[i][j][0] = 0
                    dp[i][j][1] = max(dp[i-1][j][0], dp[i-1][j][1]) - array[i]
                else:
                    # Find the minimum prime divisor of the current number
                    min_prime_divisor = find_min_prime_divisor(array[i])
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]) - array[i]
                    dp[i][j][1] = max(dp[i-1][j][0], dp[i-1][j][1])

    # Return the maximum beauty of the array
    return max(dp[n-1][n-1][0], dp[n-1][n-1][1])

def find_min_prime_divisor(num):
    for i in range(2, num+1):
        if is_prime(i) and num % i == 0:
            return i

# Read input from stdin
n, m = map(int, input().split())
array = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(array, bad_primes))
