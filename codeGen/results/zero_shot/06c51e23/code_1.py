import sys

def max_grade(n, t):
    decimal = float(input().strip())
    grade = 0
    time_spent = 0
    
    for i in range(1, n+1):
        digit = int((decimal * 10) % 10)
        
        # Calculate the new grade if we round up or down
        new_grade_up = grade + (digit >= 5)
        new_grade_down = grade + (digit < 5)
        
        # Update the maximum grade and time spent
        if new_grade_up > new_grade_down:
            grade = new_grade_up
            time_spent += 1
        elif new_grade_down > grade:
            grade = new_grade_down
            time_spent += 1
        else:
            break
        
        # Check if we've reached the time limit
        if time_spent >= t:
            break
    
    return int(grade)

n, t = map(int, input().split())
print(max_grade(n, t))
