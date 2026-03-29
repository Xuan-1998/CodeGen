n = int(input())  # read the number of days from stdin

water_level = 0
sum_below_water = 0

for _ in range(n):
    marks_above = int(input()) - water_level
    sum_below_water += marks_above
    water_level += int(input())

print(sum_below_water)  # print the minimum possible sum to stdout
