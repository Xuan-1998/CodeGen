t = [1, 2, 3]
l = 2
r = 5

result = 0
for i in range(t[0]):
    result += t[i] * f(l + i) - l * f(r)

print(result % (10**9 + 7))
