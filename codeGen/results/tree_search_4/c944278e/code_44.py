def findWinningTeams(n):
    memo = {}
    def dfs(phase):
        if phase in memo:
            return memo[phase]
        if len(memo) > 0:
            memo[0] = [""]
        else:
            memo[0] = ["0"]
        for i in range(1 << n):
            binary = bin(i)[2:].zfill(n)
            wins = 0
            for j in range(n):
                if binary[j] == '1':
                    wins += 1
                elif wins > 0:
                    memo[phase].append(binary)
                    break
    return [str(x) for x in sorted(set([int(''.join(map(lambda x: str(int(x))), teams)) for phase, teams in dfs(phase).items()]))]

n = int(input())
print(findWinningTeams(n))
