def min_marks_below_water():
    n = int(input())
    marks_above = list(map(int, input().split()))
    
    min_sum = 0
    for i in range(n):
        total_marks = i + 1
        water_level = total_marks - marks_above[i]
        min_sum += water_level
    
    print(min_sum)
