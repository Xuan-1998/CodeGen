import sys

n = int(sys.stdin.readline())  
t = [0] * n 
fare = 0 

for i in range(n):
    t[i] = int(sys.stdin.readline())  
    while t[i] % 60 >= 1:
        if t[i] // 60 < 14 * 30:  # One-trip ticket (20 BYR)
            fare += 20
        elif 14 * 30 <= t[i] // 60 < 14 * 60:  # 90-minute ticket (50 BYR)
            fare += 50
        else:  # One-day ticket (120 BYR)
            fare += 120
        t[i] %= 60  # Move to the next minute
    if t[i] >= 1:
        fare += 20  # Add one-trip ticket (20 BYR) for each trip
    print(fare)  # Print the total fare after each trip
    fare = 0  # Reset the total fare

print(fare)  # Print the total fare for the last trip
