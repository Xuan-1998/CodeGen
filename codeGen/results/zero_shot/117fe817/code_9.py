def findDigitOne(n):
    count = 0
    i = 1
    while i <= n:
        count += min(i, (n // i) + 1)
        i *= 10
    return count

if __name__ == "__main__":
    n = int(input())
    print(findDigitOne(n))
