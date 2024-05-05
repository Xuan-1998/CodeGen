n = int(input())  # read the number of days from stdin
marks_above = list(map(int, input().split()))  # read the number of marks above water for each day

total_marks = sum(marks_above)  # calculate the total number of marks
min_sum_below_water = float('inf')  # initialize the minimum sum with a large value

for i in range(n):
    m_below = i - marks_above[i]  # calculate the number of marks below water for this day
    min_sum_below_water = min(min_sum_below_water, total_marks - (i * (i + 1) // 2 + m_below))  # update the minimum sum

print(min_sum_below_water)  # print the result to stdout
