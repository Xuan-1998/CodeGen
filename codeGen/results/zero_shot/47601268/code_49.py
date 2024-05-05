python
def count_non_consecutive_ones(n):
    count = 0
    for i in range(n + 1):
        has_consecutive_ones = False
        bin_i = bin(i)[2:]  # remove '0b' prefix
        for j in range(len(bin_i) - 1):  # iterate through all bits except the last one
            if bin_i[j] == '1' and bin_i[j + 1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            count += 1

    return count
