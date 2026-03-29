def findDigitOne(n):
    bits = bin(n).count('1')
    if n < 10:
        return bits

    result = [0] * (n.bit_length() + 1)
    for i in range(1, n + 1):
        last_bit = (i & 1)
        k = len(bin(i)) - 2
        for j in range(k - 1, -1, -1):
            if ((i >> j) & 1) == last_bit:
                result[k] += 1
            else:
                break

    return sum(result)

n = int(input())
print(findDigitOne(n))
