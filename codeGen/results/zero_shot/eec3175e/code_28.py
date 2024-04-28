n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(1) if sum([i for i in arr if i % m == 0]) % m == 0 else print(0)
