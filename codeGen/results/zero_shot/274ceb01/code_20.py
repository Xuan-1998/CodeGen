import sys

n = int(sys.stdin.readline())
marks_above_water = list(map(int, sys.stdin.readline().split()))

total_marks_below_water = 0
for i, marks in enumerate(marks_above_water):
    total_marks_below_water += (i + 1) - marks

print(total_marks_below_water)
