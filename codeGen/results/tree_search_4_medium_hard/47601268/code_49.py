def find_count(n):
    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        last_bit = bin(i)[2:].count('1')
        if last_bit % 2 != 0:  # If the last bit is not '1', then the number does not have consecutive ones
            dp[i] = dp[i - 1]
        else:
            count = sum(1 for j in range(i) if bin(j)[2:].count('1') % 2 != 0)
            dp[i] = dp[i - 1] + count

    return dp[n]

n = int(input())
print(find_count(n))
