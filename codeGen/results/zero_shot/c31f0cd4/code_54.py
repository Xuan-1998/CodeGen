from itertools import chain, combinations

n = int(input())
a = list(map(int, input().split()))
all_sums = set()

for r in range(1, n+1):
    for subset in chain(*map(lambda x: combinations(a, x), range(r, 0, -1))):
        all_sums.add(sum(subset))

print(' '.join(map(str, sorted(all_sums))))
