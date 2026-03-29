def countOnes(n):
    dp = [0] * (n.bit_length() + 1)
    ones_in_n = bin(n).count('1')

    for i in range(ones_in_n, -1, -1):
        if n // (2 ** i) > 0:
            n_ones = (n // (2 ** i)) * (i + 1)
            dp[i] += n_ones
            n -= n_ones * (2 ** i)

    return sum(dp)

n = int(input())
print(countOnes(n))
