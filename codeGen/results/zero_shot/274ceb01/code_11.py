import sys

n = int(sys.stdin.readline())
marks = list(map(int, sys.stdin.readline().split()))

min_sum = sum(marks) - max(marks)
print(min_sum)
