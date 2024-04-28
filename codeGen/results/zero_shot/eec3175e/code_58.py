n, m, arr = map(int, input().split())
print(1 if any(sum(subset) % m == 0 for r in range(len(arr)+1) for subset in itertools.combinations(arr, r)) else 0)
