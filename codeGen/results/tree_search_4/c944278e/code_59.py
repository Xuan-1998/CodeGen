import sys

n = int(sys.stdin.readline())
s = [int(c) for c in sys.stdin.readline().strip()]

winners = []
for i in range(n):
    winners.append(s[i])

winners.sort()
print(*winners, sep='\n')
