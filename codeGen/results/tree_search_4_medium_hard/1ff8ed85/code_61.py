n = int(input())
dp = [False] * (n + 1)
for i in range(1, n + 1):
    if all(length % 2 == 0 for length in b[:i]):
        dp[i] = dp[i - 1]
    elif all(length % 2 != 0 for length in b[:i]):
        dp[i] = dp[i - 1]
    else:
        for j in range(i):
            if (dp[j] and ((all(length % 2 == 0 for length in b[j:i])) or 
                           (all(length % 2 != 0 for length in b[j:i])))):
                dp[i] = True
                break

if dp[-1]:
    print("YES")
else:
    print("NO")
