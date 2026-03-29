n = int(input())  # read n from stdin
marks = list(map(int, input().split()))  # read marks on each day from stdin

total_marks = sum(range(n+1))  # calculate total number of marks
min_below_water = total_marks - max(marks)  # calculate minimum possible sum of marks below the water level

print(min_below_water)  # print the answer to stdout
