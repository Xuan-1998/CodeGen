n, k = map(int, input().split())
s = input()

if k >= n:
    s = s * (k // n + 1)
    k %= n

result = s[:k]

print(result)
