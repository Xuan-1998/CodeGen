import sys

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
fraction = float(sys.stdin.readline())

max_grade = 0

for i in range(n):
    # Round the fraction at every place after the decimal point
    rounded_fractions = [f"{int(fraction * 10**i)}.{str(int((fraction * 10**i) % 1) * 10**(n-i-1))}" for _ in range(i+1)]
    
    # Calculate the maximum possible grade for each rounding scenario
    grades = []
    for rounded_fraction in rounded_fractions:
        if int(rounded_fraction) >= 5:
            grade = 9 - (len(str(int(rounded_fraction))) - 2)
        else:
            grade = int(rounded_fraction)
        
        grades.append(grade)

    # Update the maximum possible grade
    max_grade = max(max_grade, sum(grades))

print(max_grade)
