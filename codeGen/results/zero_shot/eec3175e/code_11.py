n, m, arr = map(int, input().split())
print(1 if sum(x%m for x in arr) %m ==0 else 0)
