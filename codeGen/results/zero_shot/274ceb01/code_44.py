n = int(input())
marks = list(map(int, input().split()))
min_sum = float('inf')

for i in range(1, n+1):
    below_water_marks = marks[i-1] - i
    if below_water_marks < min_sum:
        min_sum = below_water_marks

print(min_sum)
