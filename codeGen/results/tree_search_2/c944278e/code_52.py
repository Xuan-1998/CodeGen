import sys

# Function to calculate all winning teams for a given tournament result
def calculate_winning_teams(n):
    # Initialize the dp table with empty lists
    dp = [[] for _ in range(1 << n)]

    # Base case: when n = 1, there's only one team that can win
    for i in range(1 << 1):
        dp[i].append((i, 1))

    # Dynamic programming approach to fill the dp table
    for i in range(1, 1 << n):
        for j in range(n):
            # Calculate the skill level of the current team
            skill_level = sum(x for x in (1 if ((i >> j) & 1) else -1 for j in range(n)))

            # Update the dp table with the winning teams for the current state
            for prev_state in range(i):
                if dp[prev_state]:
                    for prev_team, prev_skill_level in dp[prev_state]:
                        if (skill_level > prev_skill_level or skill_level == 0) and not any(t[1] > prev_skill_level for t in dp[i - prev_state]):
                            dp[i].append((i ^ prev_state, max(prev_skill_level, skill_level)))

    # Find all winning teams with maximum skill level
    max_skill_level = max(team[1] for team in sum(dp, []))
    return [team for team in sum(dp, []) if team[1] == max_skill_level]

# Main function to read input and print the output
def main():
    n = int(sys.stdin.readline())
    s = bin(int(sys.stdin.read()))[2:].zfill(n)
    winning_teams = calculate_winning_teams(n)

    # Print all winning teams in ascending order
    for team in sorted(winning_teams):
        print(team[0])

if __name__ == "__main__":
    main()
