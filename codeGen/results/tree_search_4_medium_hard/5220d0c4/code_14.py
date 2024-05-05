def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def min_prime_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            return i
    return None

def beauty(arr, memo={}):
    if not arr:  # base case: empty array or all bad primes
        return len([x for x in arr if is_prime(x)])

    key = tuple(sorted(arr))
    if key in memo:
        return memo[key]

    max_beauty = 0
    for i, num in enumerate(arr):
        good_primes = [x for x in arr[:i] + arr[i+1:] if is_prime(x)]
        beauty_value = beauty(arr[:i] + arr[i+1:], memo) + len(good_primes)
        max_beauty = max(max_beauty, beauty_value)

    memo[key] = max_beauty
    return max_beauty

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    # Filter out bad primes from the array
    arr = [x for x in arr if not any(x == y for y in bad_primes)]

    print(beauty(arr))

if __name__ == "__main__":
    solve()
