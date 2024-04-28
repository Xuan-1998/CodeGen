code
m = int(input())
n = int(input())
nums = [int(x) for x in input().split()]

dp = {0: 1}
curr_sum = 0

for num in nums:
    curr_sum += num
    if curr_sum % m in dp:
        print(1)
        break
    if curr_sum not in dp:
        dp[curr_sum] = 1
else:
    print(0)
