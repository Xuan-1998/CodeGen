n = int(input())
marks_above_water = list(map(int, input().split()))

total_marks_below = 0
for i in range(1, n+1):
    marks_below = marks_above_water[i-1] - (i-1) if i > 1 else i
    total_marks_below += marks_below

print(total_marks_below)
