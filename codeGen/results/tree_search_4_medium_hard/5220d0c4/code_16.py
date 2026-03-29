def max_beauty(n, m):
    # Initialize memoization dictionary
    memo = {}

    def beauty(arr):
        if not arr:
            return 0

        last_good = -1
        last_bad = -1
        for i, num in enumerate(arr):
            if is_prime(num):
                last_good = i
            else:
                last_bad = i

        # Calculate the maximum beauty value without considering the last element
        max_beauty_no_last = beauty(arr[:last_good] + arr[last_bad+1:])

        # Calculate the beauty value with the last element considered
        if is_prime(arr[last_good]):
            min_prime_divisor = get_min_prime_divisor(arr[last_good])
            new_beauty = memo.get((arr, max_beauty_no_last), 0) + min_prime_divisor
        else:
            new_beauty = max_beauty_no_last

        # Store the beauty value in the memoization dictionary
        memo[(arr, new_beauty)] = new_beauty

        return new_beauty

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_min_prime_divisor(n):
        # Calculate the minimum prime divisor of a number
        min_prime = 2
        while min_prime * min_prime <= n:
            if n % min_prime == 0:
                return min_prime
            min_prime += 1
        return None

    # Main function to compute the maximum beauty value
    arr = [int(x) for x in input().split()]
    bad_primes = [int(x) for x in input().split()]

    max_beauty = 0
    for i, num in enumerate(arr):
        if is_prime(num):
            min_prime_divisor = get_min_prime_divisor(num)
            beauty_value = memo.get((arr[:i], max_beauty), 0) + min_prime_divisor
        else:
            beauty_value = max_beauty

        # Update the maximum beauty value
        max_beauty = max(max_beauty, beauty_value)

    print(max_beauty)

if __name__ == "__main__":
    n, m = map(int, input().split())
    max_beauty(n, m)
