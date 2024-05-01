=*=BEGIN SOLUTION=*=
m = int(input())
n = int(input())
arr = list(map(int, input().split()))
dp = {0: True}

for num in arr:
    for prev_sum in list(dp.keys()):
        if prev_sum + num <= m:
            dp[prev_sum + num] = (dp.get(prev_sum + num, False) or dp[prev_sum])

print(1 if any(val for val in dp.values()) else 0)
=*=END SOLUTION=*=
