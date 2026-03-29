def countDigitOne(n):
    ans = 0
    for i in range(1, n+1):
        bin_i = bin(i)[2:]
        ones = bin_i.count('1')
        if ones == 1:
            ans += 1
    return ans

n = int(input())
print(countDigitOne(n))
