n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(1 if sum(subset) % m == 0 for subset in ([], [x]) + [(i, x) for i, x in enumerate(arr)]).any()
