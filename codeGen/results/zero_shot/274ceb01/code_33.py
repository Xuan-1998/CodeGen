n = int(input())  # read the number of days from stdin

marks = list(map(int, input().split()))  # read the array of marks from stdin

# calculate the sum of marks below the water level for each day
sums = [0] * n
for i in range(1, n):
    sums[i] = sums[i-1] + (i - marks[i])

# find the minimum possible sum
min_sum = min(sums)

print(min_sum)  # print the result to stdout
