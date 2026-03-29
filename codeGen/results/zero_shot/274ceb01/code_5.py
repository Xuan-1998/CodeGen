n = int(input())
marks_above_water = list(map(int, input().split()))

min_sum_below_water = 0
for i in range(n):
    max_mark_above_water = marks_above_water[i]
    min_sum_below_water += (i + 1) - max_mark_above_water

print(min_sum_below_water)
