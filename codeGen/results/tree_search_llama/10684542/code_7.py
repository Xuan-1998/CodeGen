def getExponent(n, p):
    x = 0
    while n // p ** x >= 1:
        x += 1
    return x - 1

# Receive input from stdin and print the result to stdout.
n, p = map(int, input().split())
print(getExponent(n, p))
