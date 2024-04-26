def getExponent(n, p):
    x = 0
    while n % p == 0:
        x += 1
        n //= p
    return x if p > 1 else None

if __name__ == "__main__":
    n, p = map(int, input().split())
    print(getExponent(n, p))
