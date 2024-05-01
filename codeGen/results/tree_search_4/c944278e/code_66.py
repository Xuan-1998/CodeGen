from itertools import combinations

def tournament_winner(n, s):
    dp = {}
    winners = []

    # Initialize the dynamic programming table
    for i in range(n):
        state = tuple(1 << (n - 1 - i) for _ in range(i + 1))
        dp[state] = [state]

    # Calculate the winning teams for each phase
    for i in range(n, 0, -1):
        next_dp = {}
        for state in dp:
            winners_in_state = []
            for j in combinations(range(i), i // 2):
                next_state = tuple(x & (1 << k) for x, k in zip(state, j))
                if all(opponent < opponent_win if skill_level[opponent] > skill_level[opponent_win] else True for opponent, opponent_win in zip(j, j)):
                    winners_in_state.append(next_state)
            next_dp[state] = winners_in_state
        dp = next_dp

    # Combine the winning teams from each phase
    for state in dp:
        winners.extend(dp[state])

    return sorted(winners)

n = int(input())
s = input()
print(*tournament_winner(n, s), sep='\n')
