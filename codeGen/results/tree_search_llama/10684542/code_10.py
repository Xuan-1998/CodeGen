def get_exponent(n, p):
    exponent = 0
    while n >= p:
        n //= p
        exponent += 1
    return exponent

n, p = map(int, input().split())
print(get_exponent(n, p))
