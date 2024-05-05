t = int(input())
l = int(input())
r = int(input())

result = 0
for i in range(t):
    result += (i % t) * f(min(l + i, r))
    if i >= l:
        result -= l * f(r)

print(result % (10**9 + 7))
