n = int(input())  # read the number of days
marks_above_water = list(map(int, input().split()))  # read the array of marks above the water

minimum_sum_below_water = sum(marks_above_water)  # initialize the minimum sum with the total marks above the water

for i in range(1, n):  # for each day (starting from the second day)
    maximum_marks_above_water = max(marks_above_water[:i])  # find the maximum number of marks above the water on this day
    minimum_sum_below_water += i - maximum_marks_above_water  # add the difference between the current day and the maximum marks above the water to the minimum sum

print(minimum_sum_below_water)  # print the result
