import sys

n = int(sys.stdin.readline())

fare = 0
one_trip_used = False

for _ in range(n):
    t_i = int(sys.stdin.readline())
    
    if one_trip_used:
        # If the previous trip was long enough, use it again
        fare += 50
    else:
        # Use a single-trip ticket or start using a 90-minute ticket
        if t_i < 1:
            fare += 20
        elif not one_trip_used:
            fare += 20
            one_trip_used = True
        else:
            fare += 50
    
print(fare)
