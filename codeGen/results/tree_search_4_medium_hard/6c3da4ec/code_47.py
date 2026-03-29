def max_bitwise_or(n, s):
    dp = {}
    max_val = 0

    for i in range(1 << n):  # iterate over all possible starting indices
        for j in range(i + 1, 1 << n):  # iterate over all possible ending indices
            new_max = int(s[bin(i)[2:].zfill(n), 2) | int(s[bin(j)[2:].zfill(n)], 2)
            max_val = max(max_val, new_max)

    print(bin(max_val)[2:])
