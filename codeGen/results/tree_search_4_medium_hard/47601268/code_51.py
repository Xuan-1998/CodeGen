from sys import stdin

def count_numbers_without_consecutive_ones(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        k = len(bin(i - 1)[2:].lstrip('0'))
        if bin(i)[2:].endswith('0' * k):
            dp[i] = sum(dp[m] for m in range(k))
        else:
            dp[i] = dp[0] + sum(1 for j in range(1, i) if not (bin(j)[2:]).zfill(k).endswith('0' * k))

    return sum(dp)

n = int(stdin.readline())
print(count_numbers_without_consecutive_ones(n))
