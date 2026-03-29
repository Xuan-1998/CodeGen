n = int(input())
marks_above = [0] * (n + 1)
total_marks = 0
for i in range(1, n + 1):
    marks_above[i] = sum(range(i))
    total_marks += i

print(min((i - m) for i, m in zip(range(1, n + 1), marks_above[1:])))
