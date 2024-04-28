from collections import deque

def find_winning_teams(n, s):
    winning_teams = []
    teams = [i for i in range(2**n)]
    queue = deque([(teams[:], [])])

    while queue:
        current_state, path = queue.popleft()
        
        if len(path) == 2**n:
            winning_teams.append(tuple(sorted(path)))
        else:
            for i, team in enumerate(current_state):
                new_path = path + [team]
                new_state = current_state[:i] + current_state[i+1:]
                
                if s[i] == '0':
                    queue.append((new_state, new_path))
                elif len(new_state) < 2**n:
                    queue.append((new_state, new_path))

    return sorted(set(winning_teams))

if __name__ == "__main__":
    n = int(input())
    s = input()
    winning_teams = find_winning_teams(n, s)
    
    for team in winning_teams:
        print(team)
