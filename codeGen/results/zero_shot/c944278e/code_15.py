import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
winning_teams = set()

def backtrack(index, path):
    if index == n:
        winning_teams.add(''.join(path))
        return
    
    for i in range(n):
        if not s[i] or (index > 0 and s[i] != s[n - 1 - index]):
            new_path = list(path)
            new_path.append(str(i))
            backtrack(index + 1, new_path)

backtrack(0, [])
winning_teams = sorted(map(int, winning_teams))
print('\n'.join(map(str, winning_teams)))
