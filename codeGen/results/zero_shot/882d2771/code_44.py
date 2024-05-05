t, l, r = map(int, input().split())
total = 0

for i in range(t):
    if i == 0:
        total += f(l) * t[i] - l * f(r)
    else:
        total += f(l + i) * t[i]

print(total % (10**9 + 7))
