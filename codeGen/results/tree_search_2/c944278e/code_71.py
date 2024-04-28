def winning_teams(s, n):
    dp = {}

    def recursive_winners(s, n):
        if (s, n) in dp:
            return dp[(s, n)]

        if n == 1:
            return [int(s[0])]

        left_half = s[:n // 2]
        right_half = s[n // 2:]

        winners_left = recursive_winners(left_half, n // 2)
        winners_right = recursive_winners(right_half, n // 2)

        winning_teams = []
        for team1 in winners_left:
            for team2 in winners_right:
                if team1 > team2:  # Team 1 wins
                    winning_teams.append(team1)
                elif team2 > team1:  # Team 2 wins
                    winning_teams.append(team2)

        dp[(s, n)] = winning_teams
        return winning_teams

    return recursive_winners(s, n)


# Test the code with a sample input
n = int(input())
s = input()
winning_teams_list = winning_teams(s, n)
print("\n".join(map(str, sorted(winning_teams_list))))
