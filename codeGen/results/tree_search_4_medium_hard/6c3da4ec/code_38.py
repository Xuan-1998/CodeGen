from collections import defaultdict

def max_bitwise_or(n, s):
    memo = defaultdict(int)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if i - j <= 2:  # base case
                dp[i] = max(dp[i], int(s[j:j+i]))
            else:
                for k in range(j + 1, i):
                    memo[(j, k)] = s[j] | s[k]
                    dp[i] = max(dp[i], memo[(j, k)])

    return bin(max(dp))[2:].zfill(n)

n = int(input())
s = input()
print(max_bitwise_or(n, s))
