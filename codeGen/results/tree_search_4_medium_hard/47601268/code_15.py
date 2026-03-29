from collections import defaultdict

def solve(n):
    dp = defaultdict(int)
    dp[0] = 1
    for i in range(1, n + 1):
        if bin(i)[2:] != '':  # skip binary representation of 0
            last_bit = '0'
            count = 0
            for bit in bin(i)[2:]:  # iterate over the bits starting from second bit
                if bit == '1' and last_bit == '1':
                    break
                last_bit = bit
                count += dp.get(int(bit * (i.bit_length() - 1), 2), 0)
            else:
                dp[i] = count + 1
        else:
            dp[i] = 1

    return sum(dp.values())
