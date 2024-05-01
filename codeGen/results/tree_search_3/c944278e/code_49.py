def tournament_winner(n, s):
    # Convert binary string to integer array
    skills = [int(i) for i in bin(int(s, 2))[2:].zfill(n)]

    winning_teams = []
    memo = {}

    def dfs(phase):
        if phase >= len(skills):
            return [[], []]  # No more phases to consider

        if (phase,) in memo:
            return memo[(phase,)]

        winners, losers = [], []

        for i, skill in enumerate(skills[:phase]):
            # Check if team wins or loses based on its relative ranking
            if any(skills[j] < skill and s[j] == '1' for j in range(i)):
                winners.append(i)
            else:
                losers.append(i)

        memo[(phase,)] = (winners, losers)
        return dfs(phase + 1)

    winners, _ = dfs(0)
    print('\n'.join(map(str, sorted(winners))))
