def can_send_over_network(b):
    n = len(b)
    dp = [0] * (n + 1)

    dp[0] = 1 if b[0] == 1 else 0

    for i in range(1, n):
        dp[i] = min(dp[j] + (b[i] == len(a)) for j in range(i) if ((b[:i].count(len(a)) % 2 == 0 and i % 2 == 0) or (b[:i].count(len(a)) % 2 != 0 and i % 2 != 0)))
        
        k = i
        while dp[k] > 1:
            for j in range(k):
                if ((b[:k].count(len(a)) % 2 == 0 and k % 2 == 0) or (b[:k].count(len(a)) % 2 != 0 and k % 2 != 0)):
                    dp[k] = min(dp[j] + (b[k] == len(a)) for j in range(j))
                else:
                    break
            if k < n-1:
                i = k
        print("YES" if dp[n-1] > 0 else "NO")

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    can_send_over_network(b)
