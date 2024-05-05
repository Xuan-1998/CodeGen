import sys

n = int(input())
t = float(input())

# Convert the fraction into a string
fraction = str(t).split('.')[1]

# Initialize the maximum grade and the number of seconds used so far
max_grade = 0.0
seconds_used = 0.0

for i in range(n):
    if seconds_used + (i+1) > t:
        break

    # Rounding at this place will increase the grade, so we do it
    fraction = str(round(float(fraction), i))[(len('0.'*i)+1):]

    max_grade += 10**(-i)

    seconds_used += (i+1)

print(int(max_grade))
