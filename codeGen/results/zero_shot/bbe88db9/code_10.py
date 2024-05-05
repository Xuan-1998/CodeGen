# Step 1: Read input
n = int(input())  # number of rooms (1 ≤ n ≤ 10^3)
p_list = list(map(int, input().split()))  # list of room numbers that can be reached by using the second portal in each room

# Step 2: Initialize variables
crosses = [0]  # total number of crosses in each room
portal_moves = 0  # total number of portal moves needed to get out of the maze

# Step 3: Process each room
for i in range(1, n + 1):
    if i <= len(p_list):  # check if there's a second portal for this room
        crosses.append(crosses[i - 1] + (p_list[i - 1] % 2))  # update the total number of crosses in each room

# Step 4: Calculate the number of portal moves needed to get out of the maze
portal_moves = sum(1 for cross in crosses[1:] if cross % 2 != 0)  # count the number of times Vasya uses the second portal (odd number of crosses)

# Step 5: Print the answer modulo 10000 0007 (10^9 + 7)
print(portal_moves % 100000007)
