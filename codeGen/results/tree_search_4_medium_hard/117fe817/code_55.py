def findDigitOne(n):
    ans = 0
    for i in range(1, n+1):
        ans += count(i)
    return ans

def count(num):
    count = 0
    while num > 0:
        if num % 10 == 1:
            count += 1
        num //= 10
    return count
