import sys
n, m = map(int, input().split())
print(min((n // i + 1) * (m // j + 1) for i in range(1, min(n, m) + 1) for j in range(i, min(n, m) + 1)))
