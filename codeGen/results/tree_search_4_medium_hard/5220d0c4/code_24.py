from collections import defaultdict

def find_max_beauty(n, m, arr, bad_primes):
    dp = defaultdict(int)
    max_beauty = 0

    for i in range(n):
        if arr[i] in bad_primes:
            max_beauty += min_prime_divisor(arr[i])
        elif (i > 0 and min_prime_divisor(arr[i]) == min_prime_divisor(arr[i-1])):
            dp[i] = dp[i-1] + arr[i]
        else:
            for j in range(i+1, n):
                if is_good_prime(j) or j not in bad_primes:
                    dp[j] = max(dp.get(j, 0), dp[i] + arr[j])
                    break
        max_beauty = max(max_beauty, dp[i])

    return max_beauty

def min_prime_divisor(x):
    # implement this function to find the minimum prime divisor of x
    pass

def is_good_prime(x):
    # implement this function to check if x is a good prime number
    pass
