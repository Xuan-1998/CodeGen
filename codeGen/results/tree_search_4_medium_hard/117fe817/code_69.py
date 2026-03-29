def countOnes(n):
    ones = [0] * (n + 1)
    for k in range(1, n + 1):
        if k % 10 == 1:
            ones[k] = ones[k - 1]
        else:
            ones[k] = ones[k // 10] + (k % 10 != 1)
    return sum(ones)
