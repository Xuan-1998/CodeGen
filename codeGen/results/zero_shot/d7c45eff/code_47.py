n, k = map(int, input().split())
s = input()

if k < n:
    result = s[:k]
else:
    result = s * (k // n) + s[k % n:]

print(result)
