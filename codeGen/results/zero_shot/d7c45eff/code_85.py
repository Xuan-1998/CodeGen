n = int(input())
k = int(input())
s = input().strip()

if k >= n:
    result = s * ((k - n) // len(s) + 1)
else:
    if k < len(s):
        result = s[:k]
    else:
        result = s

print(result)
