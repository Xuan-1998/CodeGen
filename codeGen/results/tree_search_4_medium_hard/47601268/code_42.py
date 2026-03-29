=*= code *==
import sys

def count_non_consecutive_ones(n):
    dp = {0: 1}
    for i in range(1, n+1):
        if '1' not in bin(i)[2:]:
            dp[i] = 1
        else:
            prev_zero_index = None
            for bit in bin(i)[2:]:
                if bit == '1':
                    if prev_zero_index is not None:
                        break
                    prev_zero_index = len(bin(i)[2:]) - 1
                elif prev_zero_index is None:
                    prev_zero_index = len(bin(i)[2:])
            else:
                dp[i] = dp.get(prev_zero_index, 0)
    return dp[n]

n = int(sys.stdin.readline())
print(count_non_consecutive_ones(n))
=*= end code *==
