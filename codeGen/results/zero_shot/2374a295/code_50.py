k, n = map(int, input().split())
print((lambda x: 1 if x == 0 else (x * ((n - 1) // x + 1)))((k + n - 1) // k))
