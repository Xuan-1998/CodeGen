n, m = map(int, input().split())
numbers = list(map(int, input().split()))
print(1 if any(sum(subset) % m == 0 for l in range(len(numbers)+1) for subset in itertools.chain(*[combinations(numbers, r) for r in range(l+1)])) else 0)
