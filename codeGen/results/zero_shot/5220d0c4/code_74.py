n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

max_beauty = beauty(arr, bad_primes)
print(max_beauty)
