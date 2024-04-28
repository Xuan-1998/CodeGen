n = int(input())
s = input()

r = 0
t = s
for i in range(n - 1):
    if t[i] == t[i + 1]:
        r += 1
        for j in range(i, n):
            if set([t[j]]).issubset({'R', 'G', 'B'}) and not set([t[j]]).issuperset({t[i]}):
                t = t[:i] + list(set([t[j]]) - {t[i]})[0] + t[i + 1:]
                break

print(r)
print(t)
