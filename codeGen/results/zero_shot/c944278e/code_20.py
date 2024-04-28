import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
winners = set()
for i in range(2**n):
    winner = ''
    for j in range(n-1, -1, -1):
        if (i & (1 << j)):
            winner = '1' + winner
        else:
            winner = '0' + winner
    winners.add(winner)
print('\n'.join(sorted(winners)))
