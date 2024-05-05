import sys

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
fraction = float(sys.stdin.readline())

# Initialize grade and remaining time
grade = 0
remaining_time = t

while remaining_time > 0:
    # Round up at the current decimal place
    rounded_fraction = (int((10 ** n) * fraction)) / (10 ** n)
    
    # Update grade and remaining time
    grade += int(rounded_fraction)
    remaining_time -= 1
    
print(grade)
