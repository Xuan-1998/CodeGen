import sys

n = int(input().strip())
marks_above_water = list(map(int, input().strip().split()))

total_marks_above_water = sum(marks_above_water)

marks_below_water = [m - i for m, i in zip(marks_above_water, range(1, n+1))]
min_sum_marks_below_water = min(marks_below_water)

print(min_sum_marks_below_water)
