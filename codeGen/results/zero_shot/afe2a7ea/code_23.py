def mod_inverse(a, m):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = egcd(b, a % b)
            return g, x - (y * (a // b)), y

    g, x, y = egcd(m, a)
    if g != 1:
        return None
    return x % m

n = int(input())
p = pow(2, n*(n+3)//2 - n, 998244353)
mod_inverse_value = mod_inverse(2**(n+2), 998244353)

print((p * mod_inverse_value) % 998244353)
