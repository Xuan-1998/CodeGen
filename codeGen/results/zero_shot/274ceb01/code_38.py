n = int(input())  # read the number of days
marks_above = list(map(int, input().split()))  # read the number of marks above the water on each day

total_marks_below = 0
for i in range(1, n+1):
    total_marks_below += i - marks_above[i-1]

print(total_marks_below)  # print the minimum possible sum of marks below the water level
