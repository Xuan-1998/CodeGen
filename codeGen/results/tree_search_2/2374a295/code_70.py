def good_sequences(n, k):
    memo = {}
    s = [1]

    for i in range(2, n+1):
        t = []
        for j in range(len(s), 0, -1):
            if i % s[j-1] == 0:
                t.append(s[j-1])
        if not t:
            return 0
        s = t + [i]
    
    dp = [0]*(k+1)
    dp[0] = 1

    for i in range(2, n+1):
        for j in range(min(i, k), 0, -1):
            if i % s[j-1] == 0:
                dp[j] += dp[j-1]
    
    return (dp[k] + 1) % 1000000007

n, k = map(int, input().split())
print(good_sequences(n, k))
