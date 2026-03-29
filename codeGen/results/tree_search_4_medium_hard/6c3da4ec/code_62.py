def maxBitwiseOR(n, s):
    if n <= 2:
        return int(s, 2)

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = int(s[0], 2)
        else:
            dp[i] = max(dp[j - 1] if j > 0 else int(s[:j], 2) for j in range(i)) | max(dp[i - j] if i > j else int(s[j:], 2) for j in range(i))

    return bin(max(dp))[2:]

n = int(input())
s = input()
print(maxBitwiseOR(n, s))
