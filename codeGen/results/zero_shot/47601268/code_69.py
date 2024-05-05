def count_binary_strings(n):
    count = 0
    for i in range(n + 1):
        binary_str = bin(i)[2:]
        has_consecutive_ones = False
        for j in range(len(binary_str) - 1):
            if binary_str[j] == '1' and binary_str[j+1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            count += 1
    return count

n = int(input())
print(count_binary_strings(n))
