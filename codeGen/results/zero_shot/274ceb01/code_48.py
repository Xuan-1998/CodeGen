n = int(input())
marks_above = list(map(int, input().split()))
min_sum = sum(i - m - 1 for i, m in enumerate(marks_above, start=1))
print(min_sum)
