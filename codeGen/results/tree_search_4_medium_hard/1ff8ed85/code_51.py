n = int(input())
b = list(map(int, input().split()))
dp = [False] * (n + 1)
for i in range(n):
    for j in range(i+1):
        if ((i-j) % 2 == 0 and dp[j]) or ((i-j) % 2 != 0 and not dp[j]):
            if b[i] >= i-j:
                dp[i] = True
                break
print("YES" if dp[-1] else "NO")
