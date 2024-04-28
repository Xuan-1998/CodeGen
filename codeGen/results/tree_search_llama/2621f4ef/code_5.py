import sys

def calculate_area(side_length):
    # Calculate the area of the city with the given side length
    return side_length ** 2

def is_covered(mines, side_length):
    # Check if all mines are within the city boundaries
    for x, y in mines:
        if abs(x) > side_length / 2 or abs(y) > side_length / 2:
            return False
    return True

max_side = int(input())
min_side = 1
threshold = 0.001
prev_area = float('inf')

while max_side - min_side > threshold:
    side_length = (max_side + min_side) / 2
    area = calculate_area(side_length)
    
    if is_covered(mines, side_length):
        prev_area = area
        max_side = side_length
    else:
        min_side = side_length

print(prev_area)
