import sys

def count_ones(n):
    dp = {0: 0}
    for i in range(1, n+1):
        if i.bit_length() == 1:
            dp[i] = 1
        else:
            dp[i] = dp[i-1] + (i // 10**(i.bit_length()-1)) - (dp.get(i//10**(i.bit_length()-1), 0))
    return sum(dp.values())

n = int(sys.stdin.readline())
print(count_ones(n))
