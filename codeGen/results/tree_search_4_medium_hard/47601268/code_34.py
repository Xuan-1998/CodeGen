import sys

def count_binary(n):
    dp = {0: 1}
    for i in range(1, n+1):
        if bin(i).count('1') < len(bin(i))-2:
            dp[i] = dp.get(i-1, 0) + 1
        else:
            dp[i] = dp.get(i-1, 0)
    return dp.get(n, 0)

n = int(sys.stdin.readline())
print(count_binary(n))
