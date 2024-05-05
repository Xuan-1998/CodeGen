n, m = map(int, open(0).read().split()[:2])
arr = list(map(int, open(0).read().split()[2:]))
bad_primes = set(map(int, open(0).read().split()[-m:]))

max_beauty = 0
for num in arr:
    beauty = calculate_beauty(num)
    max_beauty = max(max_beauty, beauty)

print(max_beauty)
