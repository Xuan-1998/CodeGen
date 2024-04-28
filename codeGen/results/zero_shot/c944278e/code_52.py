import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
winning_teams = [i+1 for i in range(n) if bin((1<<n)-1>>i)&int(s)]
print(*sorted(winning_teams), sep='\n')
