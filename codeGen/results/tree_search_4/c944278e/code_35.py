import sys

def solve():
    n = int(input())
    s = input()
    k = 2**n - 1
    dp = {(0, '0'*n): 1}
    winning_teams = set()

    for i in range(n):
        next_dp = {}
        for prev_phase, teams in list(dp.items()):
            phase, remaining_games = prev_phase
            if int(remaining_games[-1], 2) < k:
                continue
            for j in range(2**k):
                new_phase = (phase + 1) * '1' + bin(j)[2:].zfill(n - i - 1)
                if s[i] == '1':
                    next_dp[(new_phase, new_phase)] = teams
                else:
                    next_dp[(new_phase, new_phase)] = len(teams)
        dp = next_dp

    for phase, teams in sorted(dp.items()):
        for team in range(int(phase[1:], 2)):
            if team >= k and s.count('1') == n:
                winning_teams.add(team)

    print('\n'.join(map(str, sorted(winning_teams))))

if __name__ == "__main__":
    solve()
