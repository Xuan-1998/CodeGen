import sys

def find_winning_teams(n):
    memo = {0: 1}
    for i in range(1, n+1):
        new_memo = {}
        for j in range(i):
            win_if_lose = (memo[j] << 1) | 1  # skill level of the next team if it loses
            win_if_win = memo[j] + (2**(n-i-1))
            new_memo[win_if_lose] = max(new_memo.get(win_if_lose, 0), win_if_win)
            new_memo[win_if_win] = max(new_memo.get(win_if_win, 0), win_if_lose)
        memo.update(new_memo)

    winning_teams = []
    for skill_level in range(2**n):
        if skill_level > memo.get(skill_level, 0):
            winning_teams.append(bin(skill_level)[2:].zfill(n))

    return sorted(winning_teams)

n = int(sys.stdin.readline())
print(*find_winning_teams(n), sep='\n')
