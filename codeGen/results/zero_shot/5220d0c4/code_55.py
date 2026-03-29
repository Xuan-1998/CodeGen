n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

max_beauty = 0
for i in range(1 << n):
    subset = [num for j, num in enumerate(arr) if (i & (1 << j))]
    max_beauty = max(max_beauty, beauty(subset, bad_primes))

print(max_beauty)
