import sys

def count_binary_numbers(n):
    dp = [[False, False] for _ in range(31)]  # log2(n) + 1 bits

    dp[0][0] = True
    dp[0][1] = True

    for k in range(1, len(dp)):
        for i in range(2):
            if not i:  # last bit is 0
                dp[k][i] = (dp[k-1][0] or not dp[k-1][1]) and (not dp[k-1][0] or dp[k-1][1])
            else:  # last bit is 1
                dp[k][i] = (dp[k-1][0] or dp[k-1][1]) and (not dp[k-1][0] or not dp[k-1][1])

    count = 0
    for k in range(len(dp)-1, -1, -1):
        if dp[k][0]:
            count += 2 ** k
            break

    return count

n = int(sys.stdin.readline())
print(count_binary_numbers(n))
