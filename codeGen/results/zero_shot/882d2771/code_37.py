t, l, r = map(int, input().split())
print((sum(t_i * f(l + i) for i in range(r - l + 1)) - l * f(r)) % (10**9 + 7))
