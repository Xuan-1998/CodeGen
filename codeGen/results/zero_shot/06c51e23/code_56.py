# Read input
n, t = map(int, input().split())
fraction = float(input())

# Initialize maximum grade as 0
max_grade = 0

# Loop through each digit after decimal point
for i in range(n):
    # Calculate current rounded value
    rounded_value = round(fraction * (10 ** i), 0)
    
    # Check if the time limit is exceeded
    if t - 1 >= i:  # Assuming it takes 1 second to calculate each digit
        max_grade = max(max_grade, int(rounded_value))
    else:
        break

print(max_grade)
