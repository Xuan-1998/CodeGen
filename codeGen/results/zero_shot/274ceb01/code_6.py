n = int(input())
marks_above_water = list(map(int, input().split()))

sum_marks_below = 0
for i in range(1, n+1):
    total_marks = i
    marks_below = total_marks - marks_above_water[i-1]
    sum_marks_below += marks_below

print(sum_marks_below)
