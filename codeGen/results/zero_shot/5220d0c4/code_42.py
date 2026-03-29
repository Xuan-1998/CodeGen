def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def beauty(arr, bad_primes):
    max_beauty = float('-inf')
    for i in range(len(arr)):
        if arr[i] in bad_primes:
            min_divisor = arr[i]
            is_good_prime = False
        else:
            for j in range(2, int(arr[i]**0.5) + 1):
                if arr[i] % j == 0 and not is_prime(j):
                    min_divisor = j
                    break
            if is_prime(arr[i]):
                is_good_prime = True

        beauty = arr[i] / min_divisor if is_good_prime else -arr[i]
        max_beauty = max(max_beauty, beauty)

    return max_beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(beauty(arr, bad_primes))
