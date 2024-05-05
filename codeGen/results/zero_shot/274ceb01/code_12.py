n = int(input())  # read the number of days from stdin
marks_above_water = list(map(int, input().split()))  # read the marks above water for each day

min_sum_below_water = float('inf')  # initialize minimum sum to infinity

for i in range(n):
    marks_above_water_level = marks_above_water[i]
    marks_below_water_level = i - marks_above_water_level
    min_sum_below_water = min(min_sum_below_water, marks_below_water_level)

print(min_sum_below_water)  # print the minimum possible sum of marks below water level
