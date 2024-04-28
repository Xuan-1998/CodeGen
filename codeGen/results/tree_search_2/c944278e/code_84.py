import sys

def winning_teams(n, s):
    teams = [i for i in range(2**n)]
    dp = {0: []}

    for i in range(1, 2**n):
        if s[i-1] == '1':
            winners = []
            for j in dp.get(i-1, []):
                for k in range(j+1, 2**n):
                    if sum(bin(k)[2:].zfill(n)) > sum(bin(j)[2:].zfill(n)):
                        winners.append(k)
            dp[i] = winners
        else:
            dp[i] = dp.get(i-1, [])[0:]

    return sorted(set([team for i in range(2**n) for team in dp.get(i, [])]))

# Read input from stdin
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

# Print the winning teams to stdout
print(*winning_teams(n, s), sep='\n')
