def min_sum_below_marks(n, marks_above):
    sum_below = 0
    current_marks = set()  # To keep track of the water levels where marks are made

    for i in range(n):
        mi = marks_above[i]
        # The number of marks below the water level is at least (i - mi)
        # We need to find the minimum number of new marks that must be below the water level
        new_marks_below = i - mi  # Start with the maximum possible below marks

        # Check if we can place some of these marks at the same level as previous days
        while new_marks_below in current_marks:
            new_marks_below -= 1  # Reduce the number of new marks by finding a coinciding mark

        # Add the minimum number of new marks below the water level to the sum
        sum_below += new_marks_below

        # Add the current water level to the set of marks
        current_marks.add(i - new_marks_below)

    return sum_below

# Read input from stdin
n = int(input().strip())
marks_above = list(map(int, input().strip().split()))

# Calculate and print the answer
print(min_sum_below_marks(n, marks_above))
