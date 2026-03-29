def findOnes(n):
    ones = [0] * 10
    ones[1] = 1

    for i in range(2, len(str(n)) + 1):
        ones[i % 10] += 10 ** (i - 1) * ones[(i - 1) % 10]
    return sum(ones)
