def find_max_beauty(n, m):
    memo = {}
    def max_beauty(arr, good_primes_count):
        if (arr, good_primes_count) in memo:
            return memo[(arr, good_primes_count)]
        if not arr:
            return 0 if all(x % 2 for x in bad_primes) else len(good_primes)
        if not any(x % 2 for x in arr):
            return max_beauty(arr[1:], good_primes_count + 1)
        memo[(arr, good_primes_count)] = max(
            max_beauty(arr[1:], good_primes_count),
            max_beauty(arr[1:], good_primes_count - 1) if any(x % 2 for x in arr[:1]) else 0
        )
        return memo[(arr, good_primes_count)]
    bad_primes = list(map(int, input().split()))
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_beauty(a, 0))

if __name__ == "__main__":
    find_max_beauty(0, 0)
