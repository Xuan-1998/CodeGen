def f(s):
    if s == 1:
        return 0
    p = min([i for i in range(2, int(s ** 0.5) + 1) if s % i == 0])
    if p not in b:  # good prime
        return f(s // p) + s
    else:  # bad prime
        return f(s // p) - s

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_beauty = 0

for i in range(n):
    for j in range(i+1, n):
        if a[j] % a[i] == 0:  # GCD with subset
            g = a[i]
            while g > 1:
                p = min([i for i in range(2, int(g ** 0.5) + 1) if g % i == 0])
                if p not in b:
                    g //= p
                else:
                    g -= p
            a[j] = g
    max_beauty = max(max_beauty, f(a[i]))

print(max_beauty)
