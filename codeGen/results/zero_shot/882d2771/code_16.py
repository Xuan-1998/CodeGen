code
t = int(input())
l, r = map(int, input().split())

def f(n):
    if n == 1:
        return 0
    else:
        return 1 + f(n//2)

t0 = f(l)
for i in range(1, t+1):
    ti = f(i+l-1)
    t0 += ti

result = t0 - l*f(r)
print(result % (10**9 + 7))
