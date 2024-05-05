import sys

n = int(sys.stdin.readline())
marks_above = list(map(int, sys.stdin.readline().split()))

total_marks = 0
min_sum = float('inf')

for i in range(1, n+1):
    below_water = i - marks_above[i-1] - 1
    total_marks += below_water
    if total_marks < min_sum:
        min_sum = total_marks

print(min_sum)
