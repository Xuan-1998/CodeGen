n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(1 if sum(x % m == 0 for x in arr) > 0 else 0)
