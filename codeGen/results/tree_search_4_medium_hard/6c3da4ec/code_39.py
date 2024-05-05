def maxOr(s):
    n = len(s)
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        for j in range(i):
            for k in range(j + 1, i):
                or_val = int(s[j:j+1]|s[k:i], 2)
                dp[i] = max(dp[i], dp[j] | or_val)

    return bin(max(0, dp[-1]))[2:]

# Receive input from stdin
n = int(input())
s = input()

print(maxOr(s))
