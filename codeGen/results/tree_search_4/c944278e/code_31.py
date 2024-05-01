import heapq

def winning_teams(n):
    dp = {}
    winning_teams = set()
    
    # Iterate through each phase i from 0 to n-1:
    for i in range(n.bit_length()):
        skill_levels = {}
        
        # For each team j (where 0 <= j < 2^i), calculate its skill level by summing up the bits at positions i, i-1, ..., 0 in s.
        for s in [bin(1 << j)[2:].zfill(n.bit_length()) for j in range(2**i)]:
            team_skill = sum(int(b) for b in s)
            skill_levels[team_skill] = set(range(2**i))
        
        # Add all potential winners to dp[(i, s)].
        for skill_level, teams in skill_levels.items():
            if skill_level >= len(winning_teams):
                winning_teams.update(teams)
        
        # Initialize an empty heap heap as a priority queue based on the number of teams.
        heap = [(-len(team), team) for team in winning_teams]
        heapq.heapify(heap)
        
        # Extract the winning teams from the heap and add them to dp[(i, s)].
        while heap:
            _, team = heapq.heappop(heap)
            if len(team) > 0:
                winning_teams.remove(team)
    
    return sorted(list(winning_teams))

n = int(input())
print(*winning_teams(n), sep='\n')
