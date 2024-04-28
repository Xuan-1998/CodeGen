import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
winners = []
for i in range(2**n):
    team = [0] * n
    for j in range(n):
        if (i >> j) & 1:
            team[j] = 1
    win = True
    for k in range(len(s)):
        if s[k] == 'W':
            if team[k] == 1:
                continue
            else:
                win = False
                break
        elif s[k] == 'L':
            if team[k] == 0:
                continue
            else:
                win = False
                break
    if win:
        winners.append(i)
print(*sorted(winners))
