def count_numbers_without_consecutive_ones(n):
    ans = 0
    last_zero = -1

    for i in range(n + 1):
        has_consecutive_ones = False
        ones_count = 0

        for bit in bin(i)[2:].zfill(32):  # convert to binary and pad with zeros if necessary
            if bit == '1':
                ones_count += 1
                if ones_count > 1:
                    has_consecutive_ones = True
                    break
            else:
                last_zero = i

        if not has_consecutive_ones:
            ans += 1

    return ans
