n = int(input())
marks_above_water = list(map(int, input().split()))

highest_water_level = 0
sum_below_water = 0

for i in range(n):
    current_water_level = marks_above_water[i] + 1
    highest_water_level = max(highest_water_level, current_water_level)
    sum_below_water += highest_water_level - current_water_level

print(sum_below_water)
