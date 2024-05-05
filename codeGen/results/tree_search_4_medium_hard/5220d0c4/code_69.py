from collections import defaultdict

def max_beauty(n, m, arr, bad_primes):
    memo = defaultdict(int)

    def beauty(last_element):
        min_prime_divisor = 2
        for i in range(2, int(last_element ** 0.5) + 1):
            if last_element % i == 0:
                min_prime_divisor = i
                break

        is_good_prime = last_element not in bad_primes
        state = (min_prime_divisor, is_good_prime)
        return memo[state]

    beauty_values = [0] * n
    for i in range(1, n):
        beauty_values[i] = max(beauty_values[i-1], beauty(arr[:i+1]))

    return beauty_values[-1]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))
print(max_beauty(n, m, arr, bad_primes))
