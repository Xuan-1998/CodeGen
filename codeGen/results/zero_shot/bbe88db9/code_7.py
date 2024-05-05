n = int(input())
p = list(map(int, input().split()))

room_portals = {i+1: [p[i-1], i+1] for i in range(n)}
room_portals[n+1] = [n+1, n+1]

def vasyas_journey(room):
    if room == n+1: 
        return 0 # Return 0 if Vasya reaches the target room

    crosses = 1 # Initialize number of crosses as 1
    moves = 0
    
    while True:
        if len(room_portals[room][1]) % 2 != crosses % 2: 
            room = room_portals[room][1] # Move to the other portal
        else: 
            room = room_portals[room][0] # Stay in this room or move to the first portal
        
        moves += 1
        crosses += (len(room_portals[room][1]) % 2) # Update number of crosses

    return moves

print(vasyas_journey(1) % 1000000007)
