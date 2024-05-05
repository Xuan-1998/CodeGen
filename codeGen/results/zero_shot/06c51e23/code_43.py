import sys

def max_grade(n, t):
    frac = float(input().strip())
    max_grade = int(frac)
    t -= len(str(int(frac)))
    
    for i in range(1, n+1):
        if t >= 5:  # If we have more than 4 seconds, round up
            max_grade += 1
            t -= 4
        else:  # If we don't have enough time to round up, stop here
            break
    
    return max_grade

n, t = map(int, input().split())
print(max_grade(n, t))
