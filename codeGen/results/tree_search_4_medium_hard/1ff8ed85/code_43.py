code
t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n+1):
        if i % 2 == 0:
            for j in range(i-1, -1, -1):
                if b[j] % 2 == 0 and dp[j]:
                    dp[i] = True
                    break
        else:
            for j in range(i-1, -1, -1):
                if b[j] % 2 != 0 and dp[j]:
                    dp[i] = True
                    break
    print('YES' if dp[-1] else 'NO')
endcode
