def min_marks_below_water(n, marks):
    cumulative_sum = 0
    min_possible_sum = float('inf')
    
    for i in range(1, n+1):
        cumulative_sum += marks[i-1]
        min_possible_sum = min(min_possible_sum, i * n - cumulative_sum)
    
    return min_possible_sum

n = int(input())
marks = list(map(int, input().split()))
print(min_marks_below_water(n, marks))
