   import sys

   t = int(input())
   l, r = map(int, input().split())

   dp = [0] * (r + 1)
   for i in range(1, r + 1):
       dp[i] = 1 + min(dp[j] + 1 for j in range(1, i))

   res = 0
   for i in range(t):
       if i == 0:
           res += dp[l - 1]
       else:
           res -= l * dp[r]
   print(res % (10**9 + 7))
