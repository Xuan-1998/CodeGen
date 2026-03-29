n = int(input())
marks = list(map(int, input().split()))
cum_marks = [0] * (n + 1)
min_sum = float('inf')

for i in range(n):
    cum_marks[i + 1] = marks[i]
    if i > 0:
        min_sum = min(min_sum, n - (i + 1) - cum_marks[i])

print(min_sum)
