dp = {(1, False, 0): 0}   # base case: start at room 1 with no crosses and no visits

for i in range(2, n+2):
    for (room, visited, crosses) in dp:
        if not visited and room <= i:   # if we haven't visited this room yet
            next_crosses = crosses + (1 if not visited else 0)   # update number of crosses
            next_dp = min(dp.get((i, visited or room==n+1, next_crosses), float('inf')), dp[(room, visited, crosses)] + 1)
            dp[(i, visited or room==n+1, next_crosses)] = next_dp

print(min(dp.values()) % 1000000)   # find minimum number of portal moves and print it
