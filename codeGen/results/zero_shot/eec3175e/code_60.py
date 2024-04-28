n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(1 if any(sum(subset) % m == 0 for r in range(2**n) for subset in combinations(arr, r)) else 0)
