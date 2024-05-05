from sys import stdin

def count_numbers(n):
    dp = {0: 1}
    for i in range(1, n+1):
        if '1' * (i.bit_length() - 1).bit_length() % 2 == 0:
            dp[i] = sum(dp.get(j) for j in range(i)) + 1
        else:
            dp[i] = sum(dp.get(j) for j in range(i))
    return dp[n]

n = int(stdin.readline())
print(count_numbers(n))
