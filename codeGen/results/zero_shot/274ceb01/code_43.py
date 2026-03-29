n = int(input())
marks_above = list(map(int, input().split()))

total_marks_below = 0
for mark in sorted(marks_above):
    total_marks_below += n - mark

print(total_marks_below)
