n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(1) if sum(i % m for i in arr) == 0 else print(0)
