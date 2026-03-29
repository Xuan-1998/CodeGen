import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    portals = list(map(int, input().split()))
    
    # Initialize the count of portal moves
    count = 0
    
    # Perform BFS starting from room 1
    queue = [(1, 0)]  # (room, count)
    visited = set()
    
    while queue:
        room, move_count = queue.pop(0)
        
        if room == n + 1:
            return print(move_count % 1000000007)  # Print the result
        
        if room in visited:
            continue
        
        visited.add(room)
        
        next_room = portals[room - 1]
        queue.append((next_room, move_count + 1))
    
    return None

if __name__ == "__main__":
    solve()
