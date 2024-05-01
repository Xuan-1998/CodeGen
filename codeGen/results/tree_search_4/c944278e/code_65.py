import sys

def get_winning_teams(n, s):
    winning_teams = []
    for i in range(2**n):
        teams_left = [str(bin(i)[2:].zfill(n))]
        for j in range(n-1, -1, -1):
            if (i & (1 << j)) != 0:
                teams_left.append('1')
            else:
                teams_left.append('0')

        winning_teams.append(teams_left)

    return [team for team in winning_teams if eval(''.join(team) == s)]

def main():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    
    winning_teams = get_winning_teams(n, s)
    print(*winning_teams, sep='\n')

if __name__ == "__main__":
    main()

