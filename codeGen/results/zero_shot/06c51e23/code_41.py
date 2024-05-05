grade = 0
time_spent = 0

while fraction > 0 and time_spent <= t:
    # Round the next digit
    if fraction >= 5:
        grade += 1
        fraction -= int(fraction)
    else:
        break
    
    # Update time spent
    time_spent += 1

print(grade)
