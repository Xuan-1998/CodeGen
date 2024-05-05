def min_marks_below_water(n, marks):
    max_mark_position = 0
    total_marks_below_water = 0

    for i in range(1, n+1):
        if marks[i-1] > max_mark_position:
            max_mark_position = marks[i-1]
        total_marks_below_water += sum(range(max_mark_position+1, marks[i-1]+1))

    return total_marks_below_water
