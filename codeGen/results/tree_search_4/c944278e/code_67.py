from collections import deque

def solve():
    n = int(input())
    s = input()

    # Initialize a set to store all possible states
    states = set()

    # Use dynamic programming to find all possible winning teams for each phase
    for i in range(n):
        new_states = set()
        for state in list(states):  # Use a copy of the original set
            skill_level = sum([int(c) << (n - 1 - i) for c in bin(state)[2:].zfill(n)])
            for j in range(2 ** n):
                if s[i] == '0' or ((j >> i) & 1) == (s[i] == '0'):
                    new_state = state | (1 << (n - 1 - i))
                else:
                    new_state = state ^ (1 << (n - 1 - i))

                # Add the new state to the set if it's not a losing team
                if skill_level <= 2 ** n // 2:
                    new_states.add(new_state)

        states = new_states

    winning_teams = sorted([state for state in states if bin(state)[2:].zfill(n).count('1') == n])

    # Print the winning teams
    print('\n'.join(['{}: {}'.format(i + 1, ' '.join(map(str, [int(c) << (n - 1 - j) for c in bin(team)[2:].zfill(n)]))) for i, team in enumerate(winning_teams)])

if __name__ == "__main__":
    solve()
