n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(any(sum(subset) % m == 0 for r in range(2**len(arr)) for subset in combinations(arr, r)))
