n = int(input())
k = int(input())
s = input()

if k < n:
    result = s[:k]
else:
    result = s * (k // len(s) + 1)[:k]

print(result)
