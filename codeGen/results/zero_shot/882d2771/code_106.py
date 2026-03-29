t, l, r = map(int, input().split())
# implementation of f(n) goes here
f_l = # calculate f(l)
f_r = # calculate f(r)

result = t0*f_l + t1*(f_l+1) + ... + tr - l*f_r

print(result % (10**9 + 7))
