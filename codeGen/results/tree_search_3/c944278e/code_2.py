import sys

def find_winning_teams():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    winning_teams = []
    current_team_skill = 0

    for i in range(n):
        if s[i] == '1':
            current_team_skill += (1 << i)
        else:
            current_team_skill -= (1 << i)

        if current_team_skill > 0:
            winning_teams.append(current_team_skill)
        elif current_team_skill < 0:
            winning_teams = [current_team_skill]
            break

    print(*sorted(winning_teams), sep='\n')

if __name__ == "__main__":
    find_winning_teams()
