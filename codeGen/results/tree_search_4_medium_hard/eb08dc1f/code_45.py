def count_blocks(n):
    dp = [0] * (n + 1)
    for i in range(10 ** n, -1, -1):
        pos = len(str(i))
        l = 1
        for j in str(i)[::-1]:
            if j == '0':
                break
            l += 1
        dp[pos] = (dp[pos - 1] + l) % 998244353
    return dp[1:]

n = int(input())
print(*count_blocks(n), sep=' ')
