n = int(input())
s = input()

count_r, count_g, count_b = s.count('R'), s.count('G'), s.count('B')
ans, res = max(count_r, count_g, count_b), ''

i, r, g, b = 0, count_r, count_g, count_b
while i < n:
    if r > 0 and (g == 0 or b == 0):
        res += 'R'
        r -= 1
    elif g > 0 and (r == 0 or b == 0):
        res += 'G'
        g -= 1
    else:
        res += 'B'
        b -= 1
    i += 1

print(r + g + b)
print(res)
