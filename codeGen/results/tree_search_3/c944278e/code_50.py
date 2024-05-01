def winning_teams(n, s):
    memo = {}
    winners = set()

    if n == 0:
        return [(1 << (n - 1))]

    for i in range(1 << n):  # iterate through all possible combinations
        skill_levels = []
        for j in range(n):
            if (i >> j) & 1:  # team has higher or equal skill level
                skill_levels.append(j + 1)
        total_skill = sum(skill_levels)

        if total_skill == 0:  # no team has a higher or equal skill level
            continue

        winner = max(skill_levels, key=lambda x: x) + 1
        winners.add(winner)

    return sorted(list(winners))

# Example usage:
n = int(input())  # read the integer n from stdin
s = input()  # read the binary string s of length n from stdin

winning_teams(n, s)
