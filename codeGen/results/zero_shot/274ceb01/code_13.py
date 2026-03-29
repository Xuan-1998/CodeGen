n = int(input())
marks = list(map(int, input().split()))
total_marks = sum(marks)
min_below_water = n * (n - 1) // 2 - total_marks

print(min_below_water)
