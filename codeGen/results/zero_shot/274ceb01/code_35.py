n = int(input())
marks_above = list(map(int, input().split()))
total_marks = sum(marks_above)
min_sum = 0

for i in range(n):
    min_sum += (i * (i + 1) // 2 - marks_above[i])

print(min_sum)
