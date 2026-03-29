def find_count(n):
    count = 0
    for i in range(n+1):
        has_consecutive_ones = False
        bin_str = bin(i)[2:]
        prev_bit = None
        for bit in bin_str:
            if bit == '1' and prev_bit == '1':
                has_consecutive_ones = True
                break
            prev_bit = bit
        if not has_consecutive_ones:
            count += 1
    return count

n = int(input())
print(find_count(n))
