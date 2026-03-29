import sys
t, l, r = map(int, input().split())
f_l = min(l, 1)
f_r = min(r - l + 1, 1)
for i in range(2, r):
    f_i = f(i) if f(i-1) > f(i) else (f(i-1) + f(i))
f_max = max(f_l, f_f, ..., f_r) # Calculate the maximum value
print((t0 * f_l) % (10**9 + 7) + (t1 * f_f) % (10**9 + 7) + ...)
