n = int(input())
marks_above_water = list(map(int, input().split()))
prefix_sum = [0]
cumulative_sum = 0

for mark in marks_above_water:
    cumulative_sum += mark
    prefix_sum.append(cumulative_sum)

min_marks_below_water = float('inf')

for i in range(n):
    marks_below_water = i - prefix_sum[i + 1]
    min_marks_below_water = min(min_marks_below_water, marks_below_water)

print(min_marks_below_water)
