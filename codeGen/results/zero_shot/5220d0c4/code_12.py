n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

max_beauty = 0
for num in arr:
    max_beauty = max(max_beauty, beauty(num, bad_primes))

print(max_beauty)
