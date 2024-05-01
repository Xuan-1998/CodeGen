import sys

# Function to calculate the probability of a team winning based on their skill level and the result of the current phase
def calculate_probability(team, phase):
    if s[phase-1] == '0':
        return 0.5 ** (2**team)
    else:
        return 1 - (0.5 ** (2**(n-team)))

# Function to fill in the dynamic programming table
def fill_table():
    table = [[0.0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(i+1):
            table[i][j] = max(table[i-1][k] * calculate_probability(j, i) for k in range(j))

    return table

# Function to find all teams that have a chance to win the tournament
def find_winners():
    winners = []

    for i in range(2**n):
        if any(s[j-1] == str((i >> j) & 1) for j in range(n)):
            continue
        team = bin(i).count('1')
        table[n][team] /= sum(table[n][k] for k in range(team+1))
        winners.append(team)

    return sorted(winners)

# Main function to solve the problem
def main():
    global n, s

    n = int(input())
    s = input()

    table = fill_table()
    winners = find_winners()

    print(' '.join(map(str, winners)))

if __name__ == "__main__":
    main()
