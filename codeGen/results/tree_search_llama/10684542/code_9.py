def getExponent(n, p):
    x = 0
    while True:
        if pow(p, x+1) > n:
            return x
        x += 1

if __name__ == "__main__":
    n, p = map(int, input().split())
    print(getExponent(n, p))
