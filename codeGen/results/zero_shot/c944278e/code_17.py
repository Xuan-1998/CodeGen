import sys
n = int(sys.stdin.readline())
s = str(sys.stdin.readline().strip())

winning_teams = set()

def helper(mask, index):
    if index == n:
        winning_teams.add(int(mask, 2))
        return 
    for i in range(2):
        helper(str(i) * (index - len(mask)) + mask, index+1)

helper('', 0)
print('\n'.join(map(str, sorted(winning_teams))))
