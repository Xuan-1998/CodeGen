def find_non_consecutive_ones(n):
    dp = [1]  # base case: there is only one number (0) that does not have consecutive ones

    for i in range(1, n + 1):
        prev_num_bin = bin(i - 1)[2:]  # convert previous number to binary and remove the '0b' prefix
        if all(c != '1' or c == '1' and (j == 0 or j == len(prev_num_bin) - 1) for j, c in enumerate(prev_num_bin)):
            dp.append(dp[-1] + 1)
        else:
            dp.append(dp[-1])

    return dp[-1]
