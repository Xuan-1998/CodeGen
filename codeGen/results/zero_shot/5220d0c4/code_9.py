n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

max_beauty = 0
for i in range(2 ** n):
    # Generate all possible subsets of the array
    subset = [x for j, x in enumerate(arr) if (i >> j) & 1]
    beauty = array_beauty(subset)
    max_beauty = max(max_beauty, beauty)

print(max_beauty)
