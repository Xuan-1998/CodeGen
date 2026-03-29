# Read input
n, t = map(int, input().split())
frac = float(input())

# Initialize maximum grade
max_grade = 0

# Iterate over possible rounding places
for i in range(n):
    # Calculate new fraction with i-th digit rounded
    new_frac = round(frac, i)
    
    # Check if time limit is sufficient for this rounding
    if t >= (i + 1) * 10:  # Assuming each rounding takes 10 units of time
        # Update maximum grade if the new fraction has a better grade
        max_grade = max(max_grade, int(new_frac * 100))  # Grade is out of 100

# Print result
print(max_grade)
