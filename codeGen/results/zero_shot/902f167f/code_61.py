n, m = map(int, input().split())
print(min(m // i for i in range(1, min(n, m) + 1)))
