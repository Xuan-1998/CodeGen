# Step 1: Read the input
n, t = map(int, input().split())
decimal_fraction = float(input())

# Step 2: Calculate the maximum possible grade that can be obtained within the given time limit
max_grade = 0
while t > 0:
    # Check if rounding at the current position would give a higher grade
    temp_decimal_fraction = int((10 ** n) * decimal_fraction)
    temp_grade = min(int(temp_decimal_fraction), 9)
    
    # If the calculated grade is higher, update max_grade and move to the next digit
    if temp_grade > max_grade:
        max_grade = temp_grade
        t -= n
        decimal_fraction += (10 ** -n) * (temp_decimal_fraction % 10)
    else:
        # If not, try rounding at the next position
        t -= 1
        decimal_fraction /= 10

# Step 3: Print the maximum grade that can be obtained within the given time limit
print(max_grade)
