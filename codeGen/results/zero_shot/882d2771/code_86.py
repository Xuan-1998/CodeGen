t, l, r = map(int, input().split())
total = 0
for i in range(l, r + 1):
    total += t * f(i)
total -= l * f(r)
print(total % (10**9 + 7))
