def min_marks_below_water(n, marks):
    max_marks = [0] * n  # Initialize an array to store the maximum marks above the water level
    for i in range(1, n):
        max_marks[i] = max_marks[i-1] + (i - marks[i])  # Calculate the maximum mark above the water level

    min_sum = sum(marks)  # Initialize the minimum possible sum with the total number of marks
    for i in range(n):
        min_sum -= max_marks[i]  # Subtract the maximum mark from the total to get the minimum possible sum

    return min_sum


n = int(input())  # Read the number of days from stdin
marks = list(map(int, input().split()))  # Read the marks above the water level for each day from stdin

print(min_marks_below_water(n, marks))  # Print the minimum possible sum to stdout
