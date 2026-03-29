code
n = int(input())
s = input()
max_val = 0

for i in range(n):
    for j in range(i + 1, n):
        left_substr = s[:i]
        right_substr = s[i:j]
        left_int = int(left_substr, 2)
        right_int = int(right_substr, 2)
        max_val = max(max_val, left_int | right_int)

print(format(max_val, 'b'))
