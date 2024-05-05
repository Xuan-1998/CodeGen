python
def power_mod(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return result

n = int(input())  # read n from stdin
mod = 998244353
p = [0] * (n + 1)
p[0] = 1  # P(0) is 1
for i in range(1, n + 1):
    p[i] = power_mod(mod - 1, i, mod)

print((p[n] % mod))  # print the answer to stdout
