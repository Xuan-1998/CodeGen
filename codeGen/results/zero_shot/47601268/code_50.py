def count_numbers_without_consecutive_ones(n):
    count = 0
    for i in range(2**n):
        bin_str = bin(i)[2:]
        has_consecutive_ones = False
        for j in range(len(bin_str) - 1):
            if bin_str[j] == '1' and bin_str[j+1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            count += 1
    return count

n = int(input())
print(count_numbers_without_consecutive_ones(n))
