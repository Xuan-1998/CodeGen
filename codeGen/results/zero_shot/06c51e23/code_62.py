import sys

# Read input from stdin
n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
fraction = float(sys.stdin.readline())

grade = 0
time_taken = 0

for i in range(n):
    # Calculate the time taken to round up or down at this digit
    time_needed_to_round = (i + 1) / 10  # approximate time needed to round a single digit
    
    if time_taken + time_needed_to_round > t:
        break  # cannot perform any further rounding operations, so stop here

    # Round up or down at this digit
    if fraction >= 5:  # round up
        grade += 1
        time_taken += time_needed_to_round
    elif fraction < 0.5:  # don't round
        pass
    else:  # round down
        grade -= 0.5
        time_taken += time_needed_to_round

print(int(grade))  # print the maximum possible grade as an integer
