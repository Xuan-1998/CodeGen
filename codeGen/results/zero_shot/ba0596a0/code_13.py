import sys

stones = list(map(int, sys.stdin.readline().split()))

frog_position = 0
previous_jump = 0

for i in range(1, len(stones)):
    current_stone_position = stones[i]
    
    # calculate the minimum possible distance 
    min_possible_distance = max(1, abs(current_stone_position - frog_position) - previous_jump)
    
    if current_stone_position - frog_position > min_possible_distance:
        print("NO")
        sys.exit()
    
    frog_position = current_stone_position
    previous_jump = abs(current_stone_position - frog_position)

print("YES")
