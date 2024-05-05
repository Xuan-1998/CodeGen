def max_beauty(n, m, arr, bad_primes):
    max_beauty = 0
    for num in arr:
        beauty_value = beauty(num)
        if beauty_value > max_beauty:
            max_beauty = beauty_value
    return max_beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, m, arr, bad_primes))
