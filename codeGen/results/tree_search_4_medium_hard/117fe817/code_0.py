def findNumOf1(n):
    res = 0
    for i in range(30): # since n <= 10^9, we only need to consider numbers with at most 30 digits
        count = (n // (10**i)) * (10**i - (9*(10**(i-1)))) + min(n // (10**i), 9)
        res += count
    return res

n = int(input())
print(findNumOf1(n))
