n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(1) if sum(x % m for x in arr) % m == 0 else print(0)
