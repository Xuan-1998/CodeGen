n = int(input())
k = int(input())
s = input()

if k >= n:
    result = s * (k // n) + s[:k % n]
else:
    last_char = s[-1]
    if last_char <= s[0]:
        result = s[:-1] if k < n else s
    else:
        result = s[:k]

print(result)
