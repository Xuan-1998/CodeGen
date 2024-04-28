n, m = map(int, input().split())
print(min((m + 1) // i * (n + 1) // j for i in range(1, min(n, m) + 1) for j in range(1, min(n, m) + 1)))
