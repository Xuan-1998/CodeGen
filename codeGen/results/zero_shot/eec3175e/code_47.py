n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(1 if sum(x for x in arr if x % m == 0) % m == 0 else 0)
