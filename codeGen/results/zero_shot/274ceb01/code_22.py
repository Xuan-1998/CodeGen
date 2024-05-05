def sum_marks_below_water(day_marks):
    return sum(i - mark for i, mark in enumerate(day_marks, start=1))

n = int(input())
marks_above_water = list(map(int, input().split()))

total_sum = min(sum_marks_below_water(marks_above_water))
print(total_sum)
