n = int(input())
arr = [int(i) for i in input().split()]
dp = {}
s = 0
for x in arr:
    s += x
    if s not in dp:
        dp[s] = True
    else:
        print(s, end=' ')
