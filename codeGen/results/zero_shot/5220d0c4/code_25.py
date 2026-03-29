n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = set(map(int, input().split()))

print(beauty(arr))
