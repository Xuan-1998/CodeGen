def max_beauty(n, m, arr, bad_primes):
    memo = {}

    def dfs(k):
        if k == n - 1:
            return 0

        if (k,) in memo:
            return memo[(k,)]

        min_prime = float('inf')
        beauty = 0
        for i in range(k + 1, n):
            if arr[i] not in bad_primes and is_good_prime(arr[i], k):
                min_prime = min(min_prime, get_min_prime(arr[i]))
                beauty += min_prime
            else:
                beauty -= 2

        memo[(k,)] = beauty
        return beauty

    def is_good_prime(num, k):
        # Your implementation of checking if a number is good prime
        pass

    def get_min_prime(num):
        # Your implementation of finding the minimum prime divisor of a number
        pass

    return dfs(0)

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    print(max_beauty(n, m, arr, bad_primes))
