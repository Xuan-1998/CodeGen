def countOnes(n):
    ones = [0] * 10
    for i in range(1, n+1):
        num_str = str(i)
        for j in range(len(num_str)):
            if int(num_str[j]) == 1:
                ones[len(num_str) - j - 1] += 1

    return sum(ones)
