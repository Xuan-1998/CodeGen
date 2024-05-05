import sys

def min_marks_below_water():
    n = int(sys.stdin.readline())
    marks_above_water = list(map(int, sys.stdin.readline().split()))

    # Initialize minimum sum and maximum marks above water
    min_sum = 0
    max_marks_above_water = 0

    for marks in marks_above_water:
        # Update maximum marks above water if necessary
        max_marks_above_water = max(max_marks_above_water, marks)
        
        # Add the difference between current marks and maximum marks to our sum
        min_sum += max_marks_above_water - marks

    print(min_sum)

min_marks_below_water()
