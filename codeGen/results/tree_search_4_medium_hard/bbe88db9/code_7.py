def get_out_of_maze(n, portals):
    memo = {}
    def dfs(room, used_second_portal):
        if (room, used_second_portal) in memo:
            return memo[(room, used_second_portal)]
        
        if room == n + 1:
            return 0
        
        if used_second_portal:
            next_room = portals[room - 1]
            moves = 1 + dfs(next_room, False)
        else:
            next_room1 = (room * 2) % (n + 1)
            next_room2 = room - 1
            if used_second_portal and n % 2 == 1:
                next_room = next_room1
            else:
                next_room = min(next_room1, next_room2)
            
            moves = 1 + dfs(next_room, True) if next_room != next_room1 else 1 + dfs(next_room, False)
        
        memo[(room, used_second_portal)] = moves
        return moves
    
    return dfs(1, False)
