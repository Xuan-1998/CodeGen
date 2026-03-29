import sys

n = int(sys.stdin.readline())
marks_above = list(map(int, sys.stdin.readline().split()))

min_sum = sum(marks_above[i] - i for i in range(n))
print(min_sum)
