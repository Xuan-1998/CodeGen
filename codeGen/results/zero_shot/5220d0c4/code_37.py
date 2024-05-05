def max_beauty(array):
    beauty_values = calculate_beauty(array)
    return max(beauty_values)

n, m = map(int, input().split())
array = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(array))
