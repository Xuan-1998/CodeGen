n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(any(sum(subset) % m == 0 for subset in ([],] + [[num] for num in arr])))
