n = int(input())  # read the number of rooms
rooms = [[] for _ in range(n+1)]  # create a list of portals per room
for i in range(1, n+1):
    p_i = int(input())  # read the portal leading to room p_i
    rooms[i].append(p_i)  # store the portal in the correct room

dp = [[0] * (n+1) for _ in range(2)]  # create a 2D array for dynamic programming
for i in range(1, n+1):
    for x in range(n+1):  # consider all possible numbers of crosses
        if i == 1:  # base case: room 1 can be reached with 0 or 1 cross
            dp[x%2][i] = (x==0)
        else:
            dp[1-x%2][rooms[i-1][-1]] += dp[x%2][i-1]  # apply the transition rule

print(sum(dp[1]))  # print the total number of moves modulo 10^9+7
