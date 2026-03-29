# Initialize fares
fares = [0] * n

for i in range(n):
    if trips[i] <= 60:  # less than or equal to 90 minutes
        fares[i] += 20
    elif trips[i] <= 1440:  # between 91 and 1440 minutes
        fares[i] += 50
    else:
        fares[i] += 120

# Print output
for fare in fares:
    print(fare)
