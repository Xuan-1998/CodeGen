n = int(input())  # read the number of days from stdin

marks_above = list(map(int, input().split()))  # read the marks strictly above the water for each day
cumulative_sum = [0] * (n + 1)  # initialize a cumulative sum array

for i in range(n):
    cumulative_sum[i + 1] = cumulative_sum[i] + marks_above[i]

min_sum = float('inf')  # initialize the minimum sum to infinity
for i in range(n):
    min_sum = min(min_sum, (cumulative_sum[n - 1] - cumulative_sum[i]) // (i + 1))

print(min_sum)  # print the minimum possible sum to stdout
