memo = {}

def get_winning_teams(i):
    if i not in memo:
        if s[i] == '1':
            winning_teams = {(i,)}.union({*get_winning_teams(i-1)} if i>0 else set())
        else:
            losing_teams = {tuple(range(2**n))} - {*(get_winning_teams(i-1) if i>0 else set())}
            winning_teams = {(i,)}.intersection({team for team in losing_teams})
        memo[i] = winning_teams
    return memo[i]

def main():
    n = int(input())
    s = input()
    print(*sorted(set.union(*[get_winning_teams(i) for i in range(n)])), sep='\n')

if __name__ == '__main__':
    main()
