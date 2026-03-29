import sys

n = int(input())  # read number of days from stdin
marks_above_water = list(map(int, input().split()))  # read marks above water on each day

dp = [0] * (n + 1)  # create array to store minimum possible sum up to each day
total_marks = sum(marks_above_water)

for i in range(1, n + 1):
    dp[i] = min(dp[i - 1], total_marks - marks_above_water[i - 1])  # update dp[i]

min_sum_below_water = dp[-1]
print(min_sum_below_water)  # print the minimum possible sum
